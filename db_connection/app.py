from flask import Flask

app = Flask(__name__)

app.config

@app.route('/')
def hello():
    return "Hello World"

