from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.aws_helpers import ALLOWED_EXTENSIONS

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
