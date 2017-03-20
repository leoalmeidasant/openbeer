from flask import redirect, render_template, url_for, Flask, request, \
                    flash, abort
import flask_login
from app import app
from app.controllers.client_controller import ClientController
from app.controllers.login_controller import LoginController
import json

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if LoginController.validate_login('leozin', '123'):
        flask_login.login_user(user)
        flash('logged successfully.')
        next = request.args.get('next')

        if not is_safe_url(next):
            return abort(400)
        return redirect(next or url_for('index'))
    return 'NOT AUTHORIZED!'

@app.route('/')
@flask_login.login_required
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return search()

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/read/<client_id>')
def read(client_id):
    client = ClientController.search(client_id)
    return render_template('read.html', client=client)

@app.route('/search')
def search():
    return ClientController.search()

@app.route('/save', methods=['GET', 'POST'])
def client_save():
    kwargs = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'username': request.form['username']
    }
    return ClientController.save(**kwargs)

@app.route('/update', methods=['GET', 'POST'])
def update():
    kwargs = {
        'id': request.form.get('id'),
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'username': request.form.get('username')
    }
    return ClientController.update(**kwargs)

@app.route('/delete/<client_id>')
def delete_client(client_id):
    return ClientController.delete(client_id)
