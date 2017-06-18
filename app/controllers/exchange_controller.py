from app import db
from datetime import datetime
from flask import session
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand
from app.models.exchanges import Exchanges
from app.core.dao.exchanges_dao import ExchangesDao
from app.models.item_exchange import ItemExchange
from app.core.dao.item_exchange_dao import ItemExchangeDao
from app.models.item import Item
from app.core.dao.item_dao import ItemDao

class ExchangeController(object):

    @staticmethod
    def confirm_exchange(exchange):
        exchange_dao = ExchangesDao()
        item_exchange_dao = ItemExchangeDao()
        item_dao = ItemDao()

        new_exchange = Exchanges(
            client_id=exchange['client_id'],
            status='Aguardando aprovação',
            total_value=exchange['total_value'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )

        exchange_dao.save(new_exchange)

        new_item_exchange = ItemExchange(
            item_id=exchange['item_exchange']['item_id'],
            exchange_id=new_exchange.id,
            item_to_exchange=True,
            quantity=exchange['item_exchange']['quantity'],
            total_value=exchange['item_exchange']['total_value'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )

        item_exchange_dao.save(new_item_exchange)

        if session['cart']['beers']:
            for beer in session['cart']['beers']:

                new_item = Item(
                    beer_id=beer['id'],
                    snack_id=None,
                    quantity=beer['quantity'],
                    value=beer['total_value'],
                    exchange=True,
                    type='beer',
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )

                item_dao.save(new_item)

                new_item_ex = ItemExchange(
                    item_id=new_item.id,
                    exchange_id=new_exchange.id,
                    item_to_exchange=False,
                    quantity=beer['quantity'],
                    total_value=beer['total_value'],
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )

                item_exchange_dao.save(new_item_ex)

        if session['cart']['snacks']:
            for snack in session['cart']['snacks']:

                new_item = Item(
                    beer_id=None,
                    snack_id=snack['id'],
                    quantity=snack['quantity'],
                    value=snack['total_value'],
                    exchange=True,
                    type='snack',
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )

                item_dao.save(new_item)

                new_item_ex = ItemExchange(
                    item_id=new_item.id,
                    exchange_id=new_exchange.id,
                    item_to_exchange=False,
                    quantity=snack['quantity'],
                    total_value=snack['total_value'],
                    created_at=datetime.today(),
                    updated_at=datetime.today()
                )

                item_exchange_dao.save(new_item_ex)

            return 'Pedido de troca efetuado com sucesso!'
