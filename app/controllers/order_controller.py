from app import db
from flask import session
from datetime import datetime
from flask_login import current_user
from app.models.order import Order
from app.models.item import Item
from app.models.item_order import ItemOrder
from app.models.beer import Beer
from app.models.snack import Snack
from app.models.reversal import Reversal
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand
from app.controllers.command.update_stock_command import UpdateStockCommand
from app.core.strategy.make_item_list import ItemList
from app.core.strategy.update_stock import UpdateStock
from app.core.dao.order_dao import OrderDao
from app.core.dao.return_item_dao import ReturnItensDao

class OrderController(object):

    @staticmethod
    def get_orders():
        order = Order()
        return SearchCommand.execute(order)

    def get_all():
        orders = Order.query.all()
        return orders

    def get_order_items(id):
        items = ItemOrder.query.filter(ItemOrder.order_id == id).all()
        return items

    def get_order_status(id):
        status = db.session.query(Order.status).filter(Order.id == id).first()
        return status

    def update_status(id, status):
        order_dao = OrderDao()
        result = order_dao.update_status(id, status)
        return result

    def update(order, client_id=None):
        old_order = Order.query.filter(Order.id == order['id']).first()
        updated_order = Order(
            id=order['id'],
            total_value=old_order.total_value - order['value']
        )
        result = UpdateCommand.execute(updated_order)

        item = Item.query.filter(Item.id == order['item_id']).first()

        if item.type == 'beer':
            beer = Beer(
                id=item.beer_id,
                quantity=item.quantity + int(order['quantity'])
            )
            UpdateStockCommand.execute(beer)
        else:
            snack = Snack(
                id=item.snack_id,
                quantity=item.quantity + int(order['quantity'])
            )
            UpdateStockCommand.execute(snack)

        reversal = Reversal(
            client_id=client_id,
            value=order['value']
        )
        ReturnItensDao.reversal(reversal)
        ReturnItensDao.update(order['return_id'], 'Devolução efetuada')
        return result

    @staticmethod
    def finalizing_shop():
        order = Order(
            fare=5,
            order_date=datetime.today(),
            payment_form=session['payment_form'],
            total_value=session['cart']['total'] + 5,
            status='Aguardando aprovação de pagamento',
            client_id=current_user.id,
            delivery_address_id=session['selected_address'],
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

            if item.type == 'beer':
                beer = Beer(
                    id=item.beer_id,
                    quantity=item.quantity
                )
                UpdateStockCommand.execute(beer)
            else:
                snack = Snack(
                    id=item.snack_id,
                    quantity=item.quantity
                )
                UpdateStockCommand.execute(snack)

            item_order = ItemOrder(
                item_id=item.id,
                order_id=order.id,
                created_at=datetime.today(),
                updated_at=datetime.today()
            )
            SaveCommand.execute(item_order)

            session['cart']['beers'] = []
            session['cart']['snacks'] = []
            session['cart']['total'] = 0

        return order
