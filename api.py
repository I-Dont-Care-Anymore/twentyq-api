from flask import Flask, session, request
import os

app = Flask(__name__)


@app.route("/begin", methods=['GET'])
def getBegin():
    pass


@app.route("/answer/<int:number>", methods=['POST'])
def postAnswer(number: int):
    pass


@app.route("/finish", methods=['GET'])
def getFinish():
    pass


if __name__ == "__main__":
    app.secret_key = os.urandom(16)
    app.run()
