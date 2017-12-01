from preproc import processMatrix
from model import predict
import flask
import json
from flask import request, send_from_directory


# Create the application.
app = flask.Flask(__name__, static_folder='./static')
app.config['SECRET_KEY'] = 'secret!'

@app.route('/get_digit', methods=['POST'])
def process_and_predict():
    print('recieved request')
    got = json.loads(request.data)
    processedMatrix = processMatrix(got)
    #Here is where we will call the model to predict.
    #predictedLabel = sgd_clf.predict(processedMatrix.reshape(1,-1))
    predictedLabel = predict(processedMatrix)
    print("The model predicted: {}".format(predictedLabel))
    return str(predictedLabel)
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

@app.route('/about.html')
def aboutPage():
    return flask.render_template('about.html')

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
