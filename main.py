#!/usr/bin/python3
from typing import Dict, Union
from flask import Flask, session, request, jsonify
from flask_cors import CORS
import os
from uuid import UUID, uuid4
from lru import LRU

from decisiontree import questions_tree, Node

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.urandom(24)
app.config.update(SESSION_COOKIE_HTTPONLY=False, SESSION_COOKIE_SECURE=True)

states: Dict[UUID, Union[Node, int]] = LRU(10000)


@app.route("/")
def index():
    return "Hello, World!"


# Answer a question as no/not sure/yes
@app.route("/answer/<int:number>", methods=['PUT', 'DELETE'])
def answer(number: int):
    if 'whoami' in session:
        whoami: UUID = session['whoami']
        if request.method == 'PUT':
            print(f'Advance question for session {whoami}')
            if type(states[whoami]) == Node:
                answer_json = request.get_json()['answer']
                if answer_json == 'no':
                    index = 0
                elif answer_json == 'not sure':
                    index = 1
                elif answer_json == 'yes':
                    index = 2
                states[whoami] = states[whoami].children[index]
                if type(states[whoami].value) == int:
                    states[whoami] = states[whoami].value
        elif request.method == 'DELETE':
            print(f'Go back on question for session {whoami}')
            if type(states[whoami]) == Node and states[whoami].parent is not None:
                states[whoami] = states[whoami].parent
    return ""


@app.route("/question/<int:number>", methods=['GET'])
def question(number: int):
    if number == 1 or 'whoami' not in session:
        whoami = uuid4()
        session['whoami'] = whoami
        print(f'New session {whoami}')
    else:
        whoami = session['whoami']

    if whoami not in states:
        states[whoami] = questions_tree.root

    if type(states[whoami].value) == int:
        print(f'Completed session {whoami}')
        del states[whoami].value
        return jsonify({
            'answer': states[whoami].value
        })
    else:
        print(f'Get question for session {whoami}')
        return jsonify({
            'question': f'Is your idea related to {states[whoami].value}?'
        })


if __name__ == "__main__":
    app.run()
