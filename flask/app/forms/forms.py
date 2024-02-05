from flask_wtf import FlaskForm
# input field
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, EmailField, PasswordField)
# ตัวเช็คว่ามัน validate รึป่าว
from wtforms.validators import InputRequired, Length, Email, EqualTo , Regexp

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),Length(min=2, max=20)])
    email = EmailField('Email', validators=[InputRequired(), Email(message="Invalid Email")])
    # 
    password = PasswordField('Password', validators=[InputRequired(), Regexp('.*\d.*', message="Password must contain at least one number")])
    conform_password = PasswordField('Conform Password', validators=[InputRequired(), EqualTo('password', message="Passwords must match") ])