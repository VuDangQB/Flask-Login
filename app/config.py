"""Flask configuration."""
from os import environ, path

BOILERPLATE_ENV = environ.get("BOILERPLATE_ENV", "dev")

class Config:
    """Base config."""
    APP_NAME = "Login"
    # Get absolute path to project folder
    BASE_DIR = path.dirname(path.realpath(__file__))
    SECRET_KEY = environ.get('SECRET_KEY')
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SECRET_KEY='GDtfDCFYjD'
    DB_USER = environ.get("DB_USERNAME", "root")
    DB_PASSWORD = environ.get("DB_PASSWORD", "11111111")
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_PORT = environ.get("DZ_DB_PORT", 3306)
    DB_NAME = environ.get("DZ_DB_NAME", "root")

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=DevConfig,
    prod=ProdConfig,
    server=ProdConfig
)