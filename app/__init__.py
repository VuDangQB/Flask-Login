from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_compress import Compress
from flask_login import LoginManager

from app.config import config_by_name

db = SQLAlchemy()
migrate = Migrate()
compress = Compress()
login_manager = LoginManager()

def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])