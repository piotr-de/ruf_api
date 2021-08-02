import os
from flask import Flask
from flask_httpauth import HTTPTokenAuth
from resources.routes import initialize_routes, start_loader


app = Flask(__name__)
app.config.from_pyfile('config.py')
auth = HTTPTokenAuth(scheme='Bearer')
env_token = os.environ.get('RUF_API_TOKEN')

if __name__ == '__main__':
    initialize_routes(app, auth, env_token)
    start_loader()
    app.run()
