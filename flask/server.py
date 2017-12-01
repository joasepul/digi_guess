import flask
import numpy as np
import json
import scipy.misc #requires pillow to be installed
                  #pip install pillow


from flask import request, send_from_directory

from sklearn.datasets import fetch_mldata
# Create the application.
from flask import request, send_from_directory

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import SGDClassifier
#sgd_clf = pickle.load(open("../ML_model/sgd_clf_trained_MNIST.pickle", "rb"))
from keras.models import load_model
cnn_digit_clf = load_model("../ML_model/cnn_digit_clf.h5")

# Create the application.
app = flask.Flask(__name__, static_folder='./static')
app.config['SECRET_KEY'] = 'secret!'

@app.route('/get_digit', methods=['POST'])
def process_image():
    print('recieved request')
    got = json.loads(request.data)
    image_matrix = np.array(got, dtype=np.uint8).reshape((100,100))
    #CV algorithm will be called here to seperate digits

    #Then for each digit found this the following will happen
    processed_matrix = scipy.misc.imresize(image_matrix, (28,28), interp='nearest')
    print(processed_matrix)
    #Here is where we will call the model to predict.
    processed_matrix = processed_matrix.reshape(1, 1, 28, 28).astype('float32')
    #Here is where we will call the model to predict.
    #predictedLabel = sgd_clf.predict(processedMatrix.reshape(1,-1))
    predicted_label = cnn_digit_clf.predict_classes([processed_matrix])
    print("The model predicted: {}".format(predicted_label))
    return str(predicted_label)
    #We will return whatever label the model predicts, or the answer to
    #the arithmetic expression


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
