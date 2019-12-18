# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import app_config

db = SQLAlchemy()

# user management, logging in, logging out, and user sessions.
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    # message when a user is redirected to the login page.
    login_manager.login_message = "You must be logged in to access this page."
    # redirect to auth.login view
    login_manager.login_view = "auth.login"

    # temporary route
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'

    return app