import os

from flask import Flask, g
from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        # app.config['MONGODB_SETTINGS'] = {
        #     'db': os.getenv('DB_NAME'),
        #     'host': os.getenv('DB_HOST'),
        #     # 'username': os.getenv('DB_USERNAME'),
        #     # 'password': os.getenv('DB_PASSWORD'),
        #     'connect': False
        # }
    else:
        # load the test config if passed in
        app.config.from_pyfile(test_config)

    # ensure the config folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    initialize_extensions(app)
    register_blueprints(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from src.apis import bp_api
    app.register_blueprint(bp_api)


def get_db():
    return g.db


def close_db():
    pass
