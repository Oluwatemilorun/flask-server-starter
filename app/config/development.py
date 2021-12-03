import os
from .base import Config as BaseConfig


class Config(BaseConfig):
    """Develop environment settings."""

    DEBUG = os.environ.get("DEBUG", "False") == "True"
    JSONIFY_PRETTYPRINT_REGULAR = DEBUG
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_DATABASE_URI") or "postgresql://localhost/app"
    )  # noqa

