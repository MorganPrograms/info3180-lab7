from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms import TextAreaField





class UploadForm(FlaskForm):
    description = TextAreaField('description', validators = [DataRequired()])
    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    
   

