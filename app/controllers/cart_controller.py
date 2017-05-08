from flask import session
from app import db
from datetime import datetime
from flask_login import current_user
from app.models.order import Order
from app.models.item import Item
from app.models.item_order import ItemOrder
from app.controllers.beer_controller import BeerController
from app.controllers.snack_controller import SnackController
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand
from app.core.strategy.make_item_list import ItemList
from app.core.strategy.update_stock import UpdateStock

class CartController(object):

    @staticmethod
    def add_beer_session(id):
        beer = BeerController.search(id)
        item = dict(
            id=beer.id,
            name=beer.name,
            value=beer.value,
            image=beer.image,
            quantity=session['quantity'],
            type='beer',
            total_value=int(session['quantity']) * beer.value
        )
        session['cart']['total'] += item['total_value']
        session['cart']['beers'].append(item)
        return 'Item {} adicionado ao carrinho!'.format(beer.name)

    @staticmethod
    def remove_beer_session(beer_id):
        for index, item in enumerate(session['cart']['beers']):
            if int(beer_id) == item['id']:
                session['cart']['total'] -= item['total_value']
                session['cart']['beers'].pop(index)
                return 'Item removido com sucesso!'

    @staticmethod
    def add_snack_session(id):
        snack = SnackController.search(id)
        item = dict(
            id=snack.id,
            name=snack.name,
            value=snack.value,
            image=snack.image,
            quantity=session['quantity'],
            type='snack',
            total_value=int(session['quantity']) * snack.value
        )
        session['cart']['total'] += item['total_value']
        session['cart']['snacks'].append(item)
        return 'Item {} adicionado ao carrinho!'.format(snack.name)

    @staticmethod
    def remove_snack_session(snack_id):
        for index, item in enumerate(session['cart']['snacks']):
            if int(snack_id) == item['id']:
                session['cart']['total'] -= item['total_value']
                session['cart']['snacks'].pop(index)
                return 'Item removido com sucesso!'

    @staticmethod
    def finalizing_shop():
        order = Order(
            fare=5,
            order_date=datetime.today(),
            payment_form='money',
            total_value=session['cart']['total'] + 5,
            client_id=current_user.id,
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        SaveCommand.execute(order)
        items_list = ItemList.make_list()
        for i in items_list:
            item = Item(
                item_id=i['id'],
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
                    id=item.item_id,
                    quantity=item.quantity
                )
            else:
                UpdateStock.update_snack(
                    id=item.item_id,
                    quantity=item.quantity
                )
            db.session.commit()
            session['cart']['beers'] = []
            session['cart']['snacks'] = []
            session['cart']['total'] = 0

        return 'Compra finalizada, produto em preparo para transporte!'
