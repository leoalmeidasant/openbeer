import datetime
from app import db
from flask import session
from app.models.order import Order

class OrderDao(object):

    def save(self, order):
        db.session.add(order)
        db.session.flush()
