import json

import pandas as pd
import pickle
import sklearn

class PetalPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, df):
        if self.model is None:
            self.model = pickle.load(open("model.sav", 'rb'))
        y_pred = self.model.predict(df)
        print(y_pred)
        return y_pred
