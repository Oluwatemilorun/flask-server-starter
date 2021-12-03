import os


class Config:
    # Flask's general settings
    DEBUG = False

    # SQLAlchemy's general settings
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 15
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_ALEMBIC = os.getenv("SQLALCHEMY_DATABASE_URI_ALEMBIC")
    SQLALCHEMY_DATABASE_URI_CELERY = os.getenv("SQLALCHEMY_DATABASE_URI_CELERY")

    # flask-rest-api
    OPENAPI_VERSION = "3.0.2"
