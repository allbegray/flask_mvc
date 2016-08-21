from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import *


class BoardInsertForm(Form):
    title = StringField("제목", validators=[DataRequired()])
    content = TextAreaField("내용", validators=[DataRequired()])
    submit = SubmitField('저장')
