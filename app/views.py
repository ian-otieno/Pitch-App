from app import app
from flask import render_template, flash, redirect, request, url_for
from .email import send_email
from .models import Comments, User, db, Pitch
from flask_login import current_user, login_user, logout_user, login_required
from .forms import CommentsForm, LoginForm, RegisterForm, PitchForm
from flask_bcrypt import Bcrypt
import datetime
from .token import confirm_token, generate_confirmation_token

bcrypt = Bcrypt(app)


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')