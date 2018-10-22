from collections import namedtuple
import json

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/lul', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


@app.route('/json/kek', methods=['GET'])
def reJSON():
    #stringa = '{"key":["python", "py", 2]}'
    #jsonDate = json.loads(stringa)
    return (json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
