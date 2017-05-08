import json
from app import db, app
from sqlalchemy import func
from app.models.beer import Beer
from app.models.item import Item
from flask import render_template, flash, session, jsonify
from flask_login import login_required
from app.schemas.sell_schema import SellSchema

@app.route('/dashboard')
@login_required
def dashboard():
    if session['role'] == 'admin':
        return render_template('dashboard.html.j2')
    else:
        return 401

@app.route('/sell_per_mark')
def sell_per_mark():
    data = db.session.query(Beer.mark.label('name'),\
            func.count(Beer.mark).label('y')).\
            join(Item, Item.beer_id == Beer.id).\
            group_by(Beer.mark).\
            all()
    # import ipdb; ipdb.set_trace()
    schema = SellSchema(many=True).dump(data)
    return jsonify(schema)
