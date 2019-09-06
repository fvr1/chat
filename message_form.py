from wtforms import Form, StringField
from datetime import datetime


class MessageForm(Form):
    user = StringField('User')
    text = StringField('Text')


class Message:
    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.timestamp = datetime.now().strftime('%H:%M %d/%m/%Y')
