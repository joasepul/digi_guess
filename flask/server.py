#!/usr/bin/env python
import flask
import numpy as np
import scipy.misc #requires pillow to be installed
                  #pip install pillow


from flask import request, send_from_directory
from flask_socketio import SocketIO

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import SGDClassifier
import pickle
sgd_clf = pickle.load(open("../ML_model/sgd_clf_trained_MNIST.pickle", "rb"))


# Create the application.
app = flask.Flask(__name__, static_folder='./static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#sockets
@socketio.on('init')
def success(msg):
    print(str(msg))

@socketio.on('preproc')
def processImage(arrayDict):
    got = arrayDict['data']
    imageMatrix = np.array(got, dtype=np.uint8).reshape((100,100))
    #CV algorithm will be called here to seperate digits

    #Then for each digit found this the following will happen
    processedMatrix = scipy.misc.imresize(imageMatrix, (28,28))
    #Here is where we will call the model to predict.
    predictedLabel = sgd_clf.predict(processedMatrix.reshape(1,-1))
    print("The model predicted: {}".format(predictedLabel))

    #We will return whatever label the model predicts, or the answer to
    #the arithmetic expression

    print(str(processedMatrix))

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@app.route('/index.css')
def stylesheet():
    return send_from_directory('static', 'index.css')

@app.route('/bundle.js')
def script():
    return send_from_directory('static', 'bundle.js')

@app.route('/first', methods=['POST', 'GET'])
def first():
    """ Displays the index page accessible at '/'
    """
    """return flask.render_template('index.html') """
    error = None
    if request.method == 'POST':
        return 'POST U HAVE IT'
    elif request.method == 'GET':
        return 'GET LOOKING FOR IT'
    else:
        error = 'SOMETHING DOESNT SEEM RIGHT!!!'


if __name__ == '__main__':
    app.debug=True
    socketio.run(app)
