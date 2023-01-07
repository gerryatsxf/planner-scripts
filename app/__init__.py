
from flask import Flask
from config.dev import Config as DevConfig
import os
os.environ['SCRIPT_API_ENV'] = DevConfig.SCRIPT_API_ENV
def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # from app.hello_world import api as hello_world_api
    # hello_world_api.init_app(app)

    from app.santander import api as santander_api
    santander_api.init_app(app)

    return app

