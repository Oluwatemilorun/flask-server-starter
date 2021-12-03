from flask import Flask
from flask_cors import CORS
from marshmallow import ValidationError

from app.config import config
from app.utils.extensions import args
from app.utils.response import error


def register_api_error_handlers(app: Flask) -> None:
    """
    Register error handlers for API.

    These are generic handlers that apply to all API requests.
    """

    @args.error_handler
    def handle_error(err, req, schema, status_code, headers):  # type: ignore
        raise ValidationError(err.messages)

    @app.errorhandler(ValidationError)
    def validation_error(err):  # type: ignore
        return error(errors=error.normalized_messages(), status=400)


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Note: unsafe, better set origins to known hosts
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    register_api_error_handlers(app)

    return app

