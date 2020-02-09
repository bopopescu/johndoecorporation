# __init__.py

# Third-party imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Local imports
from config import app_config

db = SQLAlchemy()
# user management, logging in, logging out, and user sessions.
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    # message when a user is redirected to the login page.
    login_manager.login_message = "You must be logged in to access this page."
    # redirect to auth.login view
    login_manager.login_view = "auth.login"

    """
    export FLASK_CONFIG=development
    export FLASK_APP=run.py
    To make this work with python3, you need to use mysqlconnector.  Install it with:
    pip install mysql-connector-python
    And change:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://dt_admin:dt2016@localhost/dreamteam_db'
    """
    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app