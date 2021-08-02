from flask import Flask
from flask_httpauth import HTTPTokenAuth
from resources.routes import initialize_routes, start_loader


app = Flask(__name__)
app.config.from_pyfile('config.py')
auth = HTTPTokenAuth(scheme='Bearer')

if __name__ == '__main__':
    initialize_routes(app, auth)
    start_loader()
    app.run()
