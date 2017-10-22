from sklearn.datasets import fetch_mldata
from sklearn.linear_model import SGDClassifier
import pickle

#get the dataset from sklearn there are 70000 data points
mnist = fetch_mldata('MNIST original')
X, y = mnist["data"], mnist["target"]
#X = digits, y = labels

#import the pickle ML model
sgd_clf = pickle.load(open("sgd_clf_trained_MNIST.pickle", "rb"))

#only index 0 - 69999
def printDigitLabel(digitIndex):
    print("The real label is: {}".format(y[digitIndex]))

digit_to_predict = 63334
    
#the reshape is just something to avoid a deprication warning
predictedLabel = sgd_clf.predict(X[digit_to_predict].reshape(1,-1))
print("The model predicted: {}".format(predictedLabel))
printDigitLabel(digit_to_predict)



