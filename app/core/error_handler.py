import json

from flask import Flask
from marshmallow import ValidationError
from sqlalchemy.exc import OperationalError

from app.utils.extensions import args
from app.utils.response import error
from app.utils.helpers import object_to_json


def init_error_handlers(app: Flask) -> None:
    """
    Register error handlers for API.

    These are generic handlers that apply to all API requests.
    """

    @args.error_handler
    def handle_error(err, req, schema, status_code, headers):  # type: ignore
        raise ValidationError(err.messages)

    @app.errorhandler(OperationalError)
    def db_error(e):  # type: ignore
        return error(errors=[object_to_json(e)], status=503)

    @app.errorhandler(ValidationError)
    def validation_error(e):  # type: ignore
        return error(errors=e.normalized_messages(), status=400)

    @app.errorhandler(404)
    def not_found(e):
        return error(message="Resource not found", status=404)
