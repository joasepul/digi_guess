from preproc import process_matrix
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
    processed_matrix = process_matrix(got)
    #Here is where we will call the model to predict.
    #predictedLabel = sgd_clf.predict(processedMatrix.reshape(1,-1))
    predicted_label = predict(processed_matrix)
    print("The model predicted: {}".format(predicted_label))
    return str(predicted_label)
    #We will return whatever label the model predicts, or the answer to
    #the arithmetic expression


@app.route('/')
@app.route('/index.html')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@app.route('/css/creative.min.css')
def stylesheet():
    return send_from_directory('static/css', 'creative.min.css')

@app.route('/about.html')
def aboutPage():
    return flask.render_template('about.html')

@app.route('/bundle.js')
def script():
    return send_from_directory('static', 'bundle.js')

if __name__ == '__main__':
    app.debug=True
