# Load libraries
import pickle
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def get_data():
    # Load dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)
    
    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    y = array[:,4]
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20)
    return(X_train, X_validation, Y_train, Y_validation)

def train_dataset(X_train, Y_train): 
    #Train model
    model = SVC(gamma='auto')
    model.fit(X_train, Y_train)
    filename = 'model.sav'
    pickle.dump(model, open(filename, 'wb'))

    
    return(model)

def do_prediction(sepalLength, sepalWidth, petalLenght, petalWidth):
        X_train, X_validation, Y_train, Y_validation = get_data()
        model = train_dataset(X_train, Y_train)
        
        ans = str(model.predict([[sepalLength, sepalWidth, petalLenght, petalWidth]])[0])
        return(ans)