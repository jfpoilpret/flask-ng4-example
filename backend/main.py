# -*- coding: utf-8 -*-

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from json import dumps

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'jfp': 'jfp'
}

todos = [
    {'id': 1, 'title': 'Hacer la compra'},
    {'id': 2, 'title': 'Poner lavadora antes del viaje'},
    {'id': 3, 'title': 'Colgar el cuadro del salón'},
]

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/todos', methods=['GET'])
@auth.login_required
def get_todos():
    return dumps(todos), 200

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
