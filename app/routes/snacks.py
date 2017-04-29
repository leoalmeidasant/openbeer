from flask import redirect, render_template, url_for, request, flash, session
from app import app, login_manager
from app.controllers.snack_controller import SnackController
from app.core.dao.user_dao import UserDao
from flask_login import login_required

@app.route('/snack')
@login_required
def snack():
    if session['role'] == 'admin':
        snacks =  SnackController.search()
        return render_template('snacks/index.html.j2',
                snacks=snacks,
                message=request.args.get('message')
            )
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/snack/new', methods=['GET', 'POST'])
@login_required
def new_snack():
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
            return SnackController.save(**kwargs)
        return render_template('snacks/new.html.j2', message=request.args.get('message'))
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/edit_snack/<id>', methods=['GET', 'POST'])
@login_required
def edit_snack(id):
    if session['role'] == 'admin':
        snack = SnackController.search(id)
        if request.method == 'GET':
            return render_template('snacks/edit.html.j2', snack=snack, message=request.args.get('message'))
        else:
            kwargs = {
                'id': id,
                'name': request.form['name'],
                'description': request.form['description'],
                'value': request.form['value'],
                'type': request.form['type'],
                'quantity': request.form['quantity'],
            }
            return SnackController.update(**kwargs)
    flash('Rota não autorizada')
    return redirect(url_for('index'))

@app.route('/delete_snack/<id>', methods=['GET', 'POST'])
@login_required
def delete_snack(id):
    if session['role'] == 'admin':
        return SnackController.delete(id)
    flash('Rota não autorizada')
    return redirect(url_for('index'))
