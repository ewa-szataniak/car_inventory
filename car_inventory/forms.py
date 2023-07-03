from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    submit_button = SubmitField()


class CarForm(FlaskForm):
    make = StringField('make')
    model = StringField('model')
    price = DecimalField('price', places=2)
    year = StringField('year')
    is_new = StringField('is_new')
    vehicle_type= StringField('vehicle_type')
    user_token = StringField('user_token')
    dad_joke = StringField('dad joke')
    submit_button = SubmitField()
