from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    data = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')