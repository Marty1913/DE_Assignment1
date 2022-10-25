import json

import pandas as pd
from flask import jsonify
import pickle
import os


class PetalPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, df):
        model_name = "model.sav"
        if self.model is None:
            self.model = pickle.load(open(model_name, 'rb'))
        y_pred = self.model.predict(df)
        return y_pred[0]
