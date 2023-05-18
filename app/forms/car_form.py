from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length

def car_make_check(form, field):
    if (len(field.data) < 1):
        raise ValidationError('Car must have a make')
    if (len(field.data) > 50):
        raise ValidationError('Car name must be 50 characters or less')

def car_description_check(form, field):
    if (len(field.data) > 400):
        raise ValidationError('Description can not be more than 400 characters.')

class CarForm(FlaskForm):
    make = StringField('make')
    model = StringField('model')
    type = StringField('type')
    year = IntegerField('year')
    mileage = IntegerField('mileage')
    price = IntegerField('price')
    color = StringField('color')
    car_description = TextAreaField('car_description')
