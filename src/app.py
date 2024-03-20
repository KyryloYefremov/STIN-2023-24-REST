from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Hello Flask </h1>"


@app.route("/time")
def get_time():
    return str(datetime.now()) + "\n"


if __name__ == '__main__':
    app.run(port=8080)
