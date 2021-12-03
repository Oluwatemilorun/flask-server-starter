import os
from .base import Config as BaseConfig

class Config(BaseConfig):
    """Production environment settings."""

    DEBUG = os.environ.get("DEBUG", "False") == "True"
    JSONIFY_PRETTYPRINT_REGULAR = DEBUG
