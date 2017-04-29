import datetime
from app import db
from app.models.snack import Snack

class SnackDao(object):

    def save(self, snack):
        db.session.add(snack)
        db.session.commit()
        return 'Produto cadastrado com sucesso!'

    def update(self, snack):
        updated = dict(
            name=snack.name,
            description=snack.description,
            value=snack.value,
            type=snack.type,
            quantity=snack.quantity,
            updated_at=datetime.datetime.now()
        )
        Snack.query.filter(Snack.id == snack.id).update(updated)
        db.session.commit()
        return 'Produto alterado com sucesso!'

    def delete(self, snack_id):
        snack = Snack.query.filter(Snack.id == snack_id).first()
        db.session.delete(snack)
        db.session.commit()
        return 'Produto deletado com sucesso!'

    def search(self, snack_id=None):
        if not snack_id:
            snacks = Snack.query.all()
            return snacks
        else:
            snack = Snack.query.filter(Snack.id == snack_id).first()
            return snack
