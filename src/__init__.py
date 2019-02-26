from flask import Flask


def creatapp():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    return app
