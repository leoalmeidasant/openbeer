import datetime
from app import db
from app.models.beer import Beer

class BeerDao(object):

    def save(self, beer):
        db.session.add(beer)
        db.session.commit()
        return 'Produto cadastrado com sucesso!'

    def update(self, beer):
        updated = dict(
            name=beer.name,
            description=beer.description,
            value=beer.value,
            type=beer.type,
            quantity=beer.quantity,
            updated_at=datetime.datetime.now()
        )
        Beer.query.filter(Beer.id == beer.id).update(updated)
        db.session.commit()
        return 'Produto alterado com sucesso!'

    def delete(self, beer_id):
        beer = Beer.query.filter(Beer.id == beer_id).first()
        db.session.delete(beer)
        return 200

    def search(self, beer_id=None):
        if not beer_id:
            beers = Beer.query.all()
            return beers
        else:
            beer = Beer.query.filter(Beer.id == beer_id).first()
            return beer
