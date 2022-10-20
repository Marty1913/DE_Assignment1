# importing Flask and other modules
import json

import requests
from flask import Flask, request, render_template

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
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # localhost or 127.0.0.1 is used when the applications are on the same machine.
        res = requests.post('http://localhost:5000/petal_predictor/', json=json.loads(json.dumps(prediction_input)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
