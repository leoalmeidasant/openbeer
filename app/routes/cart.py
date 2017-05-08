from datetime import datetime
from app import app, login_manager
from flask import session
from flask_login import login_required
from app.controllers.cart_controller import CartController
from flask import redirect, render_template, url_for, request, flash, session

@app.route('/add_beer_cart', methods=['POST'])
@login_required
def add_beer_cart():
    session['quantity'] = request.form['quantity']
    result = CartController.add_beer_session(request.form['id'])
    flash(result)
    return redirect(url_for('index'))

@app.route('/add_snack_cart', methods=['POST'])
@login_required
def add_snack_cart():
    session['quantity'] = request.form['quantity']
    result = CartController.add_snack_session(request.form['id'])
    flash(result)
    return redirect(url_for('index'))

@app.route('/remove_beer_cart/<id>')
@login_required
def remove_beer_cart(id):
    result = CartController.remove_beer_session(id)
    flash(result)
    return redirect(url_for('cart'))

@app.route('/remove_snack_cart/<id>')
@login_required
def remove_snack_cart(id):
    result = CartController.remove_snack_session(id)
    flash(result)
    return redirect(url_for('cart'))

@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html.j2')

@app.route('/resume')
@login_required
def resume():
    buy_resume = CartController.calc_cart()
    return render_template('resume.html.j2')

@app.route('/finalizing')
@login_required
def finalizing_shop():
    result = CartController.finalizing_shop()
    flash(result)
    return redirect(url_for('index'))
