#!/usr/bin/python3
""" Molule flask app """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function to return a greeting"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that displays “HBNB” """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_messages(text):
    """Function that displays c + text """
    return 'C {}'.format(text.replace('_' ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
