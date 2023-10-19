#!/usr/bin/python3
"""
Start the Flask app with root route
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    This returns a string saying Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This returns a string saying HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """
    This displays "C", followed by value of <text>
    """
    tokens = text.split("_")
    text = "C " + " ".join(tokens)
    return text


@app.route("/python",
           defaults={'text': "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text):
    """
    This displays "Python", followed by value of <text>
    """
    tokens = text.split("_")
    text = "Python " + " ".join(tokens)
    return text


@app.route("/number/<int:n>", strict_slashes=False)
def print_int(n):
    """
    This prints an integer if number passed is an int
    """
    if type(n) is int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def print_int_template(n):
    """
    This renders special HTML page if number passed is an int
    """
    if type(n) is int:
        return render_template("5-number.html", number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
