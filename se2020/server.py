from flask import Flask, jsonify
from se2020.morse import encode_morse

app = Flask(__name__)


@app.route("/")
def hello():
    payload = {"result": "Hello, world"}
    return jsonify(payload)


@app.route("/morse/<phrase>")
def encode(phrase):
    payload = {"result": encode_morse(phrase)}
    return jsonify(payload)

