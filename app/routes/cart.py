from datetime import datetime
from app import app, login_manager
from flask import session
from flask_login import login_required, current_user
from app.models.address import Address
from app.controllers.cart_controller import CartController
from app.controllers.order_controller import OrderController
from app.controllers.user_controller import UserController
from app.core.strategy.calculate_fare import CalculateFare
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

@app.route('/finalizing')
@login_required
def finalizing_shop():
    result = OrderController.finalizing_shop()
    flash('Compra efetuada com sucesso!')
    return render_template('end_buy.html.j2', order=result)

@app.route('/resume', methods=['POST'])
def resume():
    address = {
        'street': request.form.get('street'),
        'number': request.form.get('number'),
        'district': request.form.get('district'),
        'city': request.form.get('city'),
        'zip_code': request.form.get('zip_code')
    }

    session['address'] = address
    session['fare'] = CalculateFare.calculate(address['city'])

    if request.form.get('payment_form') == 'card':
        card = {
            'name': request.form.get('name'),
            'number': request.form.get('card_number'),
            'flag': request.form.get('card[type]'),
            'expiration': request.form.get('expiration'),
            'code': request.form.get('code')
        }
        session['card'] = card
        session['payment_form'] = 'Cartão'
        session['parts'] = request.form.get('parts[type]')
    else:
        session['payment_form'] = 'Dinheiro'
        session['parts'] = 'Á vista'
    return render_template('users/resume.html.j2')

@app.route('/select_address')
@login_required
def select_address():
    return render_template('users/select_address.html.j2', addresses=current_user.addresses)

@app.route('/new_address', methods=['GET', 'POST'])
@login_required
def new_address():
    if request.method == 'POST':
        address = {
            'street': request.form.get('street'),
            'number': request.form.get('number'),
            'district': request.form.get('district'),
            'city': request.form.get('city'),
            'zip_code': request.form.get('zip_code'),
            'user_id': current_user.id
        }
        result = UserController.new_address(**address)
        flash(result)
        return redirect(url_for('select_address'))
    return render_template('users/new_address.html.j2')

@app.route('/att_cart/<index>')
def att_cart(index):
    addresses = Address.query.filter(Address.user_id == current_user.id).all()
    session['selected_address'] = addresses[int(index)].id
    return render_template('cart.html.j2', index=int(index), addresses=addresses)

@app.route('/select_card')
def select_card():
    return render_template('users/select_card.html.j2')

@app.route('/admin/orders')
def admin_orders():
    orders = OrderController.get_all()
    return render_template('orders_panel.html.j2', orders=orders)
