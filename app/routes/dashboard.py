import json
from app import db, app
from sqlalchemy import func, funcfilter
from app.models.beer import Beer
from app.models.item import Item
from app.models.order import Order
from app.models.user import User
from app.models.item_order import ItemOrder
from flask import render_template, flash, session, jsonify
from flask_login import login_required
from app.schemas.sell_schema import SellSchema
from app.controllers.dashboard_controller import DashboardoController

@app.route('/dashboard')
@login_required
def dashboard():
    if session['role'] == 'admin':
        return render_template('dashboard.html.j2')
    else:
        return 401

@app.route('/sell_per_mark')
def sell_per_mark():
    dbc = DashboardoController()
    response = dbc.sell_per_mark()
    return jsonify(response)

@app.route('/sell_by_gender/', methods=['GET'])
def sell_by_gender():
    dbc = DashboardoController()
    response = dbc.sell_by_gender()
    return jsonify(response)

@app.route('/sell_by_weekday', methods=['GET'])
def sell_by_weekday():
    dbc = DashboardoController()
    response = dbc.get_sell_by_weekday()
    return jsonify(response)
