import unittest
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import User, db
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_heroku import Heroku

mail = Mail()
login = LoginManager()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = os.environ.get('SQLALCHEMY_DATABASE_URL')

load_dotenv('.env')
app.config.from_pyfile('config.py')

heroku = Heroku(app)
migrate = Migrate(app, db)

db = SQLAlchemy(app)
db.init_app(app)

login.init_app(app)
login.login_view = 'login'

mail.init_app(app)
bcrypt = Bcrypt(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app import views

tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner().run(tests)
