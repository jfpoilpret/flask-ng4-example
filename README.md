# flask-ng4-example

## Backend

Es necesario tener instalado:

- [Python 2 / 3](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

Nos posicionamos en el directorio correspondiente:

```bash
$ cd backend
```

Creamos e iniciamos un **virtualenv**; en caso de querer usar uno que ya tengamos disponible, nos saltamos el primer paso:

```bash
$ virtualenv mi-venv
$ source mi-venv/bin/activate
```

Instalamos dependencias:

```bash
$ pip install -r requirements.txt
```

Iniciamos el servidor Flask:

```bash
$ python main.py
```

## Frontend

Es necesario tener instalado:

- [Node.js](https://nodejs.org/)
- [Angular CLI](https://cli.angular.io/)

Nos posicionamos en el directorio correspondiente:

```bash
$ cd frontend
```

Instalamos dependencias:

```bash
$ npm install
```

Iniciamos el servidor web:

```bash
$ ng serve
```
