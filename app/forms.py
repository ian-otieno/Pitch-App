from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField(label='Email Address', validators=[DataRequired(), Email(message=' Please Enter A Valid Email Address!')], render_kw={"placeholder": "Email Address"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=250,  message='Password strength must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Password"})
    submit = SubmitField(label=('Log In'))

class RegisterForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired(), Length(min=2, max=250,  message='Name length must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "First Name"})
    last_name = StringField(label='Last Name', validators=[DataRequired(), Length(min=2, max=250,  message='Name length must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Last Name"})
    email = StringField(label='Email Address', validators=[DataRequired(), Email(message='Enter A Valid Email Address!')], render_kw={"placeholder": "Email Address"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=250,  message='Password strength must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password', message='The Passwords Entered Do Not Match!')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField(label=('Sign Up'))
    
class PitchForm(FlaskForm):
    pitch_body = TextAreaField(label='Pitch',validators=[DataRequired(), Length(min=5, max=250,  message='Pitch length must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Your Pitch", 'rows': 5})
    category = SelectField(label='Select Category',choices=[
        ('Creative Pitches', 'Creative Pitches'),
        ('Business Pitches', 'Business Pitches'),
        ('Interview Pitches', 'Interview Pitches'),
        ('Sales Pitches', 'Sales Pitches'),
        ('Product Pitches', 'Product Pitches')
    ], render_kw={"placeholder": "Choose Category"})
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField(label = 'Comment',validators=[DataRequired(), Length(min=5, max=250,  message='Comment length must be between %(min)d and %(max)d characters!')], render_kw={"placeholder": "Your Comment", 'rows': 5})
    submit= SubmitField('Submit')    
