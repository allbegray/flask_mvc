from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import *


class BoardInsertForm(Form):
    id = HiddenField("id")
    title = StringField("제목", validators=[DataRequired()])
    content = TextAreaField("내용", validators=[DataRequired()])
    submit = SubmitField('저장')
