import os

from flask import Flask

from instance.config import app_config

def create_app(config_name):
    ''' method for creating the app using the configurationsin the config file '''

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    from app.api.v1 import v1
    app.register_blueprint(v1)
    
    return app