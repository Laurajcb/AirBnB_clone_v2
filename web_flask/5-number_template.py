#!/usr/bin/python3
""" Molule flask app """


from flask import Flask, render_template

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
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_messages(text):
    """Function that displays python + text """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def n_messages(n):
    """ Function that displays is a nunber with a giving number """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def template_messages(n):
    """ Function that retuns HTML if is int"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
