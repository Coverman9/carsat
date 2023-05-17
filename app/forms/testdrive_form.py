from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField
from datetime import date

class TestdriveForm(FlaskForm):
    start_date = DateField('Start Date',default=date.today)
    end_date = DateField('End Date',default=date.today)

    def validate_on_submit(self):
        result = super(TestdriveForm, self).validate()
        if (self.start_date.data > self.end_date.data):
            return False
        else:
            return result
