from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField(label='Email Address', validators=[DataRequired(), Email(message=' Please Enter A Valid Email Address!')], render_kw={"placeholder": "Email Address"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=250,  message='Password strength must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Password"})
    submit = SubmitField(label=('Log In'))
