import json
import os

import pandas as pd
from flask import jsonify
import pickle


class PetalPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        if self.model is None:
            model_repo = os.environ['MODEL_REPO']
            if model_repo:
                file_path = os.path.join(model_repo, "model.sav")
                self.model = pickle.load(open(file_path, 'rb'))
            else:
                self.model = pickle.load(open("model.sav", 'rb'))
        print(json.dumps(prediction_input))
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        print(df)
        y_pred = self.model.predict(df)
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(y_pred[0])}), 200
