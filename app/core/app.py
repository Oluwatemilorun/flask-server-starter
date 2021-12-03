from flask import Flask
from flask_cors import CORS

from app.config import config


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Note: unsafe, better set origins to known hosts
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app

