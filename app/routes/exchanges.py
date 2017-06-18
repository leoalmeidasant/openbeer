import json
from app import app
from flask import redirect, render_template, url_for, Flask, request, flash, session
from flask_login import login_required, current_user
from app.controllers.exchange_controller import ExchangeController

@app.route('/exchanges/request', methods=['POST'])
@login_required
def confirm_exchange_request():
    exchange = dict(
        client_id=current_user.id,
        total_value=float(request.form.get('total_value')) - session['cart']['total'],
        item_exchange=dict(
            item_id=request.form.get('item_id'),
            quantity=request.form.get('quantity'),
            total_value=request.form.get('total_value')
        )
    )
    result = ExchangeController.confirm_exchange(exchange)
    flash(result)
    session['cart']['beers'] = []
    session['cart']['snacks'] = []
    return redirect(url_for('buys'))
