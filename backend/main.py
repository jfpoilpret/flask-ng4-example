# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from json import dumps

app = Flask(__name__)
CORS(app)

todos = [
    {'id': 1, 'title': 'Hacer la compra'},
    {'id': 2, 'title': 'Poner lavadora antes del viaje'},
    {'id': 3, 'title': 'Colgar el cuadro del salón'},
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return dumps(todos), 200


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
