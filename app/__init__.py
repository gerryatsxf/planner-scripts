from config.dev import Config as DevConfig
import os
os.environ['SCRIPT_API_ENV'] = DevConfig.SCRIPT_API_ENV

from flask import Flask
from flask_restx import Api

def create_app(config_class=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(
        title='Script API',
        version='1.0',
        description='API dedicated to running Python scripts.'
    )

    from app.hello_world import ns as ns1
    api.add_namespace(ns1)
    
    from app.santander import ns as ns2
    api.add_namespace(ns2)

    api.init_app(app)

    return app

