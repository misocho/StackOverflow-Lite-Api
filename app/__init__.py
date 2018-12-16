import os

from flask import Flask

from instance.config import app_config
from .api.v1.views.users_views import auth

def create_app(config_name):
    ''' method for creating the app using the configurationsin the config file '''

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    from app.api import v1
    app.register_blueprint(auth)

    return app