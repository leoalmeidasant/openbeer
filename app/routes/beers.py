from flask import redirect, render_template, url_for, Flask, request, flash, session
from app import app, login_manager
from app.controllers.user_controller import UserController
from app.controllers.beer_controller import BeerController
from app.models.login_form import LoginForm
from app.core.dao.user_dao import UserDao
from flask_login import login_user, logout_user, login_required, current_user
import json

@app.route('/beer')
@login_required
def beer():
    if session['role'] == 'admin':
        beers =  BeerController.search()
        return render_template('beers/index.html.j2',
                beers=beers,
                message=request.args.get('message')
            )
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/beer/new', methods=['GET', 'POST'])
@login_required
def new_beer():
    if session['role'] == 'admin':
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
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/edit_beer/<id>', methods=['GET', 'POST'])
@login_required
def edit_beer(id):
    if session['role'] == 'admin':
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
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/delete_beer/<id>', methods=['GET', 'POST'])
@login_required
def delete_beer(id):
    if session['role'] == 'admin':
        return BeerController.delete(id)
    flash('Rota não autorizada')
    return redirect(url_for('index'))
################### Fim das rotas para cervejas#################################
