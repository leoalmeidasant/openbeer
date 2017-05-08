from app import db
from app.models.item import Item

class ItemDao(object):

    def save(self, item):
        db.session.add(item)
        db.session.flush()
