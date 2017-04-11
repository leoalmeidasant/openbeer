from flask import redirect, render_template, url_for, Flask, request, flash
from app import app, login_manager
from app.controllers.client_controller import ClientController
from app.models.login_form import LoginForm
from app.core.dao.client_dao import ClientDao
from flask_login import login_user, logout_user
import json

@login_manager.user_loader
def load_user(id):
    client = ClientController
    return client.search(client_id=id)


@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('home.html.j2')

##rotas para produtos
@app.route('/product/new')
def new_product():
    return render_template('products/new.html.j2')


##rotas para admin
@app.route('/admin/new')
def new_admin():
    return render_template('admin/new.html.j2')

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
        'email': request.form['email']
    }
    return ClientController.save(**kwargs)

@app.route('/update', methods=['GET', 'POST'])
def update():
    print(request.form)
    kwargs = {
        'id': request.form.get('id'),
        'name': request.form.get('name'),
        'email': request.form.get('email')
    }
    return ClientController.update(**kwargs)

@app.route('/delete/<client_id>')
def delete_client(client_id):
    return ClientController.delete(client_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    dao = ClientDao()
    form = LoginForm()
    if form.validate_on_submit():
        user = dao.validate_login(form.email.data)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for('index'))
        else:
            flash("Invalid login.")
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("logged out.")
    return redirect(url_for('index'))
