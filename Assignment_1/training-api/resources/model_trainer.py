import logging
import os

from flask import jsonify
import pickle
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def train(dataset):
  # Split-out validation dataset
  array = dataset.values
  X = array[:,0:4]
  y = array[:,4]
  X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20)

  #Train model
  model = SVC(gamma='auto')
  model.fit(X_train, Y_train)
  
  filename = 'model.sav'
  
  model_repo = os.environ['MODEL_REPO']
  if model_repo:
      file_path = os.path.join(model_repo, filename)
      pickle.dump(model, open(file_path, 'wb'))
      logging.info("Saved the model to the location : " + model_repo)
      return jsonify(text_out), 200
  else:
      pickle.dump(model, open(filename, 'wb'))
      return jsonify({'message': 'The model was saved locally.'}), 200
