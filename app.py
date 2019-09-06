from flask import Flask, request, render_template, redirect, url_for
from message_form import MessageForm, Message
import requests
import os

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

@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(application.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)