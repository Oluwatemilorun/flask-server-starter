from flask import Flask
from flask_cors import CORS

from app.config import config
from app.api import init_api

from .error_handler import init_error_handlers
from .db import init_db


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Note: unsafe, better set origins to known hosts
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    init_error_handlers(app)
    init_db(app)
    init_api(app)

    return app

