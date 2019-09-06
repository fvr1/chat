from flask import Flask, request, render_template, redirect, url_for
from flask_paginate import Pagination, get_page_args
from message_form import MessageForm, Message
import requests
import os

application = Flask(__name__)
all_messages = []


def get_messages(offset=0, per_page=5):
    return all_messages[offset: offset + per_page]


@application.route('/', methods=["POST", "GET"])
def home():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        message = Message(form.user.data, form.text.data)
        all_messages.insert(0, message)
        return redirect('/')

    res = requests.get('https://dog.ceo/api/breeds/image/random')
    res = res.json()

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pag_messages = get_messages(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=10, total=len(all_messages),
                            css_framework='bootstrap3')

    return render_template('index.html', 
                            form=form, 
                            messages=pag_messages,
                            image=res['message'],
                            page=page,
                            per_page=per_page,
                            pagination=pagination
                            )


# codigo obtenido de https://stackoverflow.com/questions/21714653/flask-css-not-updating
# para actualizar las statics files
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