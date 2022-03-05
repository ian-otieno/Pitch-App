from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()

# Create User model that is comprised of id [Auto Generated], first_name, last_name, email and password

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(20), unique=True)
    last_name = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(55), unique=True)
    password = db.Column(db.String(250), unique=True)
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments',backref = 'user',lazy = "dynamic")
    registered_on = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    
def __init__(self, first_name, last_name, email, password, confirmed, confirmed_on=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
   

   