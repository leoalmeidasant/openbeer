from app import db
from app.models.exchanges import Exchanges

class ExchangesDao(object):

    def save(self, exchange):
        db.session.add(exchange)
        db.session.commit()
