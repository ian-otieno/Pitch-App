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
@app.route('/', methods=['POST','GET'])
def home():
    pitches = Pitch.query.all()
    user = current_user._get_current_object()
    form = PitchForm()
    if form.validate_on_submit():
        pitch_body = form.pitch_body.data
        category = form.category.data
        user_id = current_user._get_current_object().id

        pitch_obj = Pitch(user_id = user_id, pitch_body = pitch_body, category = category)
        db.session.add(pitch_obj)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('Index.html', form = form, pitches = pitches, user = user)
