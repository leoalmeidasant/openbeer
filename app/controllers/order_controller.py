from app import db
from flask import session
from datetime import datetime
from flask_login import current_user
from app.models.order import Order
from app.models.item import Item
from app.models.item_order import ItemOrder
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand
from app.core.strategy.make_item_list import ItemList
from app.core.strategy.update_stock import UpdateStock

class OrderController(object):

    @staticmethod
    def get_orders():
        order = Order()
        return SearchCommand.execute(order)

    def get_order_items(id):
        items = ItemOrder.query.filter(ItemOrder.order_id == id).all()
        return items

    @staticmethod
    def finalizing_shop():
        order = Order(
            fare=5,
            order_date=datetime.today(),
            payment_form='money',
            total_value=session['cart']['total'] + 5,
            status='aguardando pagamento',
            client_id=current_user.id,
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        SaveCommand.execute(order)
        items_list = ItemList.make_list()
        for i in items_list:
            if i['type'] == 'beer':
                item = Item(
                    beer_id=i['id'],
                    quantity=i['quantity'],
                    value=i['total_value'],
                    type=i['type'],
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )
            else:
                item = Item(
                    snack_id=i['id'],
                    quantity=i['quantity'],
                    value=i['total_value'],
                    type=i['type'],
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )

            SaveCommand.execute(item)

            item_order = ItemOrder(
                item_id=item.id,
                order_id=order.id,
                created_at=datetime.today(),
                updated_at=datetime.today()
            )
            db.session.add(item_order)

            if item.type == 'beer':
                UpdateStock.update_beer(
                    id=item.beer_id,
                    quantity=item.quantity
                )
            else:
                UpdateStock.update_snack(
                    id=item.snack_id,
                    quantity=item.quantity
                )
            db.session.commit()
            session['cart']['beers'] = []
            session['cart']['snacks'] = []
            session['cart']['total'] = 0

        return order
