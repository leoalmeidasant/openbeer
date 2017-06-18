from app import db
from app.models.item_exchange import ItemExchange

class ItemExchangeDao(object):

    def save(self, item_exchange):
        db.session.save(item_exchange)
        db.session.commit()
