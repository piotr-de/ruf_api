import os
from flask import Flask
from resources.routes import initialize_routes, start_loader


app = Flask(__name__)
app.config.from_pyfile('config.py')


if __name__ == '__main__':
    initialize_routes(app)
    start_loader()
    print(os.environ.get('FLASK_TOKEN'))
    app.run()
