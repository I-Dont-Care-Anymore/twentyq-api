#!/usr/bin/python3
from flask import Flask, session, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

# Answer a question as no/not sure/yes
@app.route("/answer/<int:number>", methods=['PUT', 'DELETE'])
def answer(number: int):
    return


@app.route("/question/<int:number>", methods=['GET'])
def question(number: int):
    return jsonify({
        'question': 'Is your product related to commercial fishing?'
    })


if __name__ == "__main__":
    app.secret_key = os.urandom(16)
    app.run()
