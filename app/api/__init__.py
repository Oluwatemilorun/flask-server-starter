from flask import Flask

from .v1 import api_v1_bp


def init_api(app: Flask):
    app.register_blueprint(api_v1_bp, url_prefix="/v1")
