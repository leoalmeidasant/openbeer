from flask import redirect, render_template, url_for, Flask, request, flash, session
from app import app, login_manager
from app.controllers.user_controller import UserController
from app.controllers.order_controller import OrderController
from app.models.login_form import LoginForm
from app.core.dao.user_dao import UserDao
from flask_login import login_user, logout_user, login_required, current_user


@login_manager.user_loader
def load_user(id):
    user = UserController
    return user.search(user_id=id)


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
                'city': request.form['city'],
                'zip_code': request.form['zip_code']
            }
        }
        return UserController.save(**user)
    return render_template('users/new.html.j2')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    dao = UserDao()
    form = LoginForm()
    if form.validate_on_submit():
        user = dao.validate_login(email=form.email.data)
        if user and user.password == form.password.data:
            login_user(user)
            session['role'] = user.role
            session['cart'] = {}
            session['cart']['beers'] = []
            session['cart']['snacks'] = []
            session['cart']['total'] = 0
            if user.role == 'admin':
                flash("Logged in as admin")
                return redirect(url_for('beer'))
            flash("Logged in.")
            return redirect(url_for('index'))
        else:
            flash("Invalid login.")
    return render_template('login.html.j2', form=form)


@app.route('/logout')
def logout():
    session.pop('role', None)
    session.pop('cart', None)
    logout_user()
    flash('Logged out!')
    return redirect(url_for('index'))


@app.route('/buys')
@login_required
def buys():
    orders = OrderController.get_orders()
    return render_template('users/buys.html.j2', orders=orders.result)

@app.route('/buy_details/<id>')
def buy_details(id):
    items = OrderController.get_order_items(id)
    # import ipdb; ipdb.set_trace()
    return render_template('users/details.html.j2', items=items)
