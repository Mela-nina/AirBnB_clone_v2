#!/usr/bin/python3
"""
Start the Flask app with root route
"""

from flask import Flask
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
