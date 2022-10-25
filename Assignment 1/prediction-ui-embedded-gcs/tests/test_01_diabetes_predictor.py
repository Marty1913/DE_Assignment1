# content of test_sysexit.py
import os
import pytest
import pandas as pd

# content of test_class.py
import petal_predictor


class TestPetalPredictor:

    @pytest.fixture(scope="session", autouse=True)
    def execute_before_any_test(self):
        os.environ["MODEL_NAME"] = "testResources/model.sav"

    # your setup code goes here, executed ahead of first test
    def test_predict_single_record(self):
        with open('testResources/prediction_request.json') as json_file:
            data = pd.read_json(json_file)
        pp = petal_predictor.PetalPredictor()
        status = pp.predict_single_record(data)
        assert bool(status[0]) is not None
