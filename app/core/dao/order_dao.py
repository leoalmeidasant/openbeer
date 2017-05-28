import datetime
from app import db
from flask import session
from flask_login import current_user
from app.models.order import Order
from app.models.item import Item
from app.models.item_order import ItemOrder


class OrderDao(object):

    def save(self, order):
        db.session.add(order)
        db.session.flush()

    def search(self, order_id=None):
        if not order_id:
            orders = db.session.query(Order).\
                filter(Order.client_id == current_user.id).\
                join(ItemOrder, ItemOrder.order_id == Order.id).\
                join(Item, Item.id == ItemOrder.item_id).all()
        else:
            orders = Order.query.all()

        return orders

    def update(self, order):
        Order.query.filter(Order.id == order.id).update(order)
        db.session.commit()
        return 'Extorno efetuado'

    def update_status(self, id, status):
        updated = dict(
            status=status
        )
        Order.query.filter(Order.id == id).update(updated)
        db.session.commit()
        return 'Status atualizado com sucesso!'
