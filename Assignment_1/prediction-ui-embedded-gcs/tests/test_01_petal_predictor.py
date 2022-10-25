# content of test_sysexit.py
import pandas as pd

# content of test_class.py
import petal_predictor


class TestPetalPredictor:
    def test_predict_single_record(self):
        with open('testResources/prediction_request.json') as json_file:
            data = pd.read_json(json_file)
        pp = petal_predictor.PetalPredictor()
        status = pp.predict_single_record(data)
        assert status[0] is not None
