import datetime
from app import db
from app.models.return_itens import ReturnItens
from app.models.reversal import Reversal

class ReturnItensDao(object):

    @staticmethod
    def save(return_item):
        db.session.add(return_item)
        db.session.commit()
        return 'ok'

    @staticmethod
    def update(id, status):
        update = dict(
            status=status
        )
        ReturnItens.query.filter(ReturnItens.id == id).update(update)
        db.session.commit()
        print('------------------------ Devolução efetuada--------------------')

    @staticmethod
    def reversal(reversal):
        db.session.add(reversal)
        db.session.commit()
