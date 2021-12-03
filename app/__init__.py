import os

from app.core.app import create_app

config_name = os.getenv("FLASK_ENV") or "development"

application = create_app(config_name)
