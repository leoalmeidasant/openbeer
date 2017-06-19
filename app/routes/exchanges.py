import json
from app import app
from sqlalchemy import desc, asc
from flask import redirect, render_template, url_for, Flask, request, flash, session
from flask_login import login_required, current_user
from app.controllers.exchange_controller import ExchangeController
from app.models.exchanges import Exchanges
from app.models.item_exchange import ItemExchange

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
    return redirect(url_for('buys'))

@app.route('/admin/exchanges', methods=['GET', 'POST'])
@login_required
def admin_exchanges():
    trades = Exchanges.query.order_by(desc(Exchanges.id)).all()
    return render_template('admin/exchanges.html.j2', trades=trades)

@app.route('/admin/approve_trade', methods=['GET', 'POST'])
@login_required
def approve_trade():
    trade_id = request.form.get('trade_id')
    result = ExchangeController.approve_trade(trade_id)
    flash(result)
    return redirect(url_for('admin_exchanges'))
