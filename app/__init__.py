from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import User, db
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_heroku import Heroku


# Initializing application
app = Flask(__name__)

from app import views