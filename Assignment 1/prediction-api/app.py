from flask import Flask, request

from petal_predictor import PetalPredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/petal_predictor/', methods=['POST']) # path of the endpoint. Except only HTTP POST request
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_inout = request.get_json()
    return pp.predict_single_record(prediction_inout)


pp = PetalPredictor()
app.run(host='0.0.0.0', port=5000)

