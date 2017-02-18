from flask import redirect, render_template, url_for, request
from app import app
from app.controllers.client_controller import ClientController
import json

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return search()

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/update/<client_id>')
def update(client_id):
    client = ClientController.search(client_id)
    return render_template('read.html', client=client)


@app.route('/search')
def search():
    return ClientController.search()

@app.route('/save', methods=['GET', 'POST'])
def client_save():
    kwargs = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    return ClientController.save(**kwargs)
