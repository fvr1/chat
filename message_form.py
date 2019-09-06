from wtforms import Form, StringField, validators
from datetime import datetime


class MessageForm(Form):
    user = StringField('User', validators=[validators.Length(min=2, max=250)])
    text = StringField('Text', validators=[validators.Length(min=2, max=250)])


class Message:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.timestamp = datetime.now().strftime('%H:%M %d/%m/%Y')
