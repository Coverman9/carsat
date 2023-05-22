from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields import StringField
from datetime import date

class TestdriveForm(FlaskForm):
    testdrive_date = StringField('Testdrive Date',default=date.today)
