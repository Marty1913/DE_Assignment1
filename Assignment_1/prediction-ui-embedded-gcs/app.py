# importing Flask and other modules
import json
import os

import requests
import pandas as pd
from flask import Flask, request, render_template, jsonify

from petal_predictor import PetalPredictor

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkpetal', methods=["GET", "POST"])
def check_petal():
    if request.method == "POST":
         prediction_input = [
            {
                "sepalLength": int(request.form.get("sepalLength")),
                "sepalWidth": int(request.form.get("sepalWidth")),
                "petalLenght": int(request.form.get("petalLenght")),
                "petalWidth": int(request.form.get("petalWidth"))
            }
        ]
        print(prediction_input)
        pp = PetalPredictor()
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        status = pp.predict_single_record(df)
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200

    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
