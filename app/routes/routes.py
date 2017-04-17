from flask import redirect, render_template, url_for, Flask, request, flash
from app import app, login_manager
from app.controllers.user_controller import UserController
from app.controllers.beer_controller import BeerController
from app.models.login_form import LoginForm
from app.core.dao.user_dao import UserDao
from flask_login import login_user, logout_user
import json

@login_manager.user_loader
def load_user(id):
    user = UserController
    return user.search(user_id=id)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    beers = BeerController.search()
    return render_template('home.html.j2', beers=beers)

##r############## Rotas para cervejas
@app.route('/beer')
def beer():
    beers =  BeerController.search()
    return render_template('beers/index.html.j2',
            beers=beers,
            message=request.args.get('message')
        )

@app.route('/beer/new', methods=['GET', 'POST'])
def new_beer():
    if request.method == 'POST':
        kwargs = {
            'name': request.form['name'],
            'description': request.form['description'],
            'value': request.form['value'],
            'type': request.form['type'],
            'quantity': request.form['quantity'],
            'image': request.files.get('image')
        }
        return BeerController.save(**kwargs)
    return render_template('beers/new.html.j2', message=request.args.get('message'))

@app.route('/edit_beer/<id>', methods=['GET', 'POST'])
def edit_beer(id):
    beer = BeerController.search(id)
    if request.method == 'GET':
        return render_template('beers/edit.html.j2', beer=beer, message=request.args.get('message'))
    else:
        kwargs = {
            'id': id,
            'name': request.form['name'],
            'description': request.form['description'],
            'value': request.form['value'],
            'type': request.form['type'],
            'quantity': request.form['quantity'],
        }
        return BeerController.update(**kwargs)

@app.route('/delete_beer/<id>', methods=['GET', 'POST'])
def delete_beer(id):
    return BeerController.delete(id)
################### Fim das rotas para cervejas

##rotas para admin
@app.route('/admin/new', methods=['GET', 'POST'])
def new_admin():
    return render_template('admin/new.html.j2')

# @app.route('/insert')
# def insert():
#     return render_template('insert.html')
#
# @app.route('/read/<user_id>')
# def read(user_id):
#     user = UserController.search(user_id)
#     return render_template('read.html', user=user)
#
# @app.route('/search')
# def search():
#     return UserController.search()
#
# @app.route('/save', methods=['GET', 'POST'])
# def user_save():
#     # kwargs = {
#     #     'name': request.form['name'],
#     #     'lastname': request.form['lastname'],
#     #     'email': request.form['email'],
#     #     'password': request.form['password'],
#     #     'confirm_password': request.form['confirm_password'],
#     #     'phone': request.form['phone'],
#     #     'level': request.form['level']
#     # }
#     return UserController.save(request.form)
#
# @app.route('/update', methods=['GET', 'POST'])
# def update():
#     print(request.form)
#     kwargs = {
#         'id': request.form.get('id'),
#         'name': request.form.get('name'),
#         'email': request.form.get('email')
#     }
#     return UserController.update(**kwargs)
#
# @app.route('/delete/<user_id>')
# def delete_user(user_id):
#     return UserController.delete(user_id)
#

@app.route('/login', methods=['GET', 'POST'])
def login():
    dao = UserDao()
    form = LoginForm()
    if form.validate_on_submit():
        user = dao.validate_login(email=form.email.data)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for('index'))
        else:
            flash("Invalid login.")
    return render_template('login.html.j2', form=form)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        user = {
            'name': request.form['name'],
            'lastname': request.form['lastname'],
            'email': request.form['email'],
            'password': request.form['password'],
            'confirm_password': request.form['confirm_password'],
            'phone': request.form['phone'],
            'address': {
                'street': request.form['street'],
                'number': request.form['number'],
                'district': request.form['district'],
                'zip_code': request.form['zip_code']
            }
        }
        return UserController.save(**user)
    return render_template('users/new.html.j2')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('index'))
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     dao = UserDao()
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = dao.validate_login(form.email.data)
#         if user and user.password == form.password.data:
#             login_user(user)
#             flash("Logged in.")
#             return redirect(url_for('index'))
#         else:
#             flash("Invalid login.")
#     return render_template('login.html', form=form)
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     flash("logged out.")
#     return redirect(url_for('index'))
