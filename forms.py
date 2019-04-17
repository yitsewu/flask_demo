from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm

class ExampleForm(FlaskForm):
    username = StringField('帳號')
    password = PasswordField('密碼')
    submit = SubmitField('登入')