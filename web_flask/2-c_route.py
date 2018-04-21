#!/usr/bin/python3
''' Starts Flask web app and listens on 0.0.0.0 on port 5000'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Prints message Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Print HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''displays C followed by value of text variable'''
    spaced_text = text.replace('_', ' ')
    return 'C % s' % spaced_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
