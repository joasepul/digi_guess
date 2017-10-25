#!/usr/bin/env python
import flask

from flask import request



# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    """ Displays the index page accessible at '/'                                                                                                                                    
    """
    return flask.render_template('index.html')


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
    app.run()

