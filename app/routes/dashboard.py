from flask import redirect, render_template, url_for, request, flash, session
from app import app, login_manager
from app.controllers.beer_controller import BeerController
from flask_login import login_required
from app.models.order import Order
from app import db

@app.route('/dashboard')
@login_required
def dashboard():
    if session['role'] == 'admin':
        return render_template('dashboard.html.j2')
    else:
        return 401

@app.route('/most_buy_week')
def most_buy_week():
    pass
