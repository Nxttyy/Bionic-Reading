from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    data = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')
