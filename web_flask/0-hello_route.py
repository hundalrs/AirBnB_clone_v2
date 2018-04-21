#!/usr/bin/python3
''' Starts Flask web app and listens on 0.0.0.0 on port 5000'''

from flask import Flask

app = Flask(__name__, strict_slashes=False)


@app.route('/')
def hello_hbnb():
    '''Prints message Hello HBNB!'''
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
