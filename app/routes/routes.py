from flask import redirect, render_template, url_for, request
from app import app

from app.controllers.client_controller import ClientController

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register_client')
def register_client():
    return render_template('register.html')

@app.route('/save', methods=['GET', 'POST'])
def client_save():
    kwargs = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    return ClientController.save(**kwargs)
