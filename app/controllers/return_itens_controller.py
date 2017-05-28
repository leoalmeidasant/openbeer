from app import db
from datetime import datetime
from app.models.item_order import ItemOrder
from app.models.return_itens import ReturnItens
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand


class ReturnItensController(object):

    @staticmethod
    def request_return(return_item):
        ItemOrder.query.filter(
            ItemOrder.item_id == return_item.item_id
        ).update(dict(returned=True))
        db.session.commit()
        result = SaveCommand.execute(return_item)
        return result
