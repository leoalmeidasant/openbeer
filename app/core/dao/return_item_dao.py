import datetime
from app import db
from app.models.return_itens import ReturnItens

class ReturnItensDao(object):

    @staticmethod
    def save(return_item):
        db.session.add(return_item)
        db.session.commit()
        return 'ok'
