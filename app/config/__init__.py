import os

from .development import Config as DevelopmentConfig
from .production import Config as ProductionConfig

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
