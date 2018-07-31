# -*- coding: utf-8 -*-

import json
import falcon

users = {
    'jfp': 'jfp'
}

todos = [
    {'id': 1, 'title': 'Hacer la compra'},
    {'id': 2, 'title': 'Poner lavadora antes del viaje'},
    {'id': 3, 'title': 'Colgar el cuadro del salón'},
]

def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class Todo(object):
    def on_get(self, req, resp):
        resp.body = json.dumps(todos, ensure_ascii =  False)

app = falcon.API()
app.add_route('/todos', Todo())

