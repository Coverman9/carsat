from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class ReviewForm(FlaskForm):
    review = StringField('review', validators=[DataRequired(), Length(max=10000, message='Review can not exceed 10,000 characters.')])
    stars = IntegerField('stars')
