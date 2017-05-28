import datetime
from app import db
from flask import session
from flask_login import current_user
from app.models.order import Order
from app.models.item import Item
from app.models.item_order import ItemOrder


class ItemOrderDao(object):

    def save(self, item_order):
        db.session.add(item_order)
        db.session.commit()

    def search(self, id):
        item_order = db.session.query(ItemOrder).filter(ItemOrder.id == id).first()
        return item_order

    def update(self, item_order):
        ItemOrder.query.filter(ItemOrder.id == item_order.id).update(item_order)
        return 'ok'
