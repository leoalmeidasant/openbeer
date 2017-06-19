from app import db
from app.models.address import Address

class AddressDao(object):

    def save(self, address):
        db.session.add(address)
        db.session.commit()
        return 'Salvo com sucesso!'
