from flask import Flask

flash_app = Flask(__name__)


@flash_app.route("/")
def hello_world():
    return "Hello World!"
