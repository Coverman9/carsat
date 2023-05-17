from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class WishlistForm(FlaskForm):
    description = StringField('description', validators=[DataRequired(), Length(max=10000, message='Description can not exceed 10,000 characters.')])
