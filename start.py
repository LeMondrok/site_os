from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Messages = namedtuple('Message', 'text tag')
messagess = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/lul', methods=['GET'])
def main():
    return render_template('main.html', messages=messagess)


@app.route('/add_message', methods=['POST'])
def add_messages():
    text = request.form['text']
    tag = request.form['tag']

    messagess.append(Messages(text, tag))

    return redirect(url_for('main'))
