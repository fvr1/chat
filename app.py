from flask import Flask, request, render_template, redirect
from src.message_form import MessageForm, Message
import requests

application = Flask(__name__)
all_messages = []

@application.route('/', methods=["POST", "GET"])
def home():
    form = MessageForm(request.form)
    if request.method == 'POST':
        message = Message(form.user.data, form.text.data)
        all_messages.append(message)
    res = requests.get('https://dog.ceo/api/breeds/image/random')
    res = res.json()
    return render_template('index.html', 
                            form=form, 
                            messages=all_messages[:100],
                            image=res['message']
                            )