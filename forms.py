from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
  comment =  StringField("Input", validators=[DataRequired()])
  submit = SubmitField("Submit")
  date =  StringField("Time")