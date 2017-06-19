from app import db, app
from sqlalchemy import func, funcfilter, extract, asc, desc
from app.models.beer import Beer
from app.models.item import Item
from app.models.order import Order
from app.models.user import User
from app.models.item_order import ItemOrder
from app.schemas.weekday_sell_schema import WeekdaySchema

class DashboardDao(object):

    def get_sells_per_mark(self):
        data = db.session.query(Beer.mark.label('name'),\
                func.count(Beer.mark).label('y')).\
                join(Item, Item.beer_id == Beer.id).\
                join(ItemOrder, ItemOrder.item_id == Item.id).\
                filter(ItemOrder.confirm_return == False).\
                group_by(Beer.mark).\
                all()
        return data

    def get_sells_by_gender(self):
        data = db.session.query(Beer.mark,
            funcfilter(func.sum(Item.quantity), User.gender == 'Masculino').label('masculino'),
            funcfilter(func.sum(Item.quantity), User.gender == 'Feminino').label('feminino')).\
                join(Item, Item.beer_id == Beer.id).\
                join(ItemOrder, ItemOrder.item_id == Item.id).\
                join(Order, Order.id == ItemOrder.order_id).\
                join(User, User.id == Order.client_id).\
                filter(ItemOrder.confirm_return == False).\
                group_by(Beer.mark).all()
        return data

    def get_sell_by_weekday(self):
        data = db.session.query(extract('dow', Order.created_at).label('dias'),
        Beer.mark, func.sum(Item.quantity).label('quantidade')).\
            join(ItemOrder, ItemOrder.order_id == Order.id).\
            join(Item, Item.id == ItemOrder.item_id).\
            join(Beer, Beer.id == Item.beer_id).\
            filter(ItemOrder.confirm_return == False).\
            group_by('dias').\
            group_by(Beer.mark).\
            order_by(asc(Beer.mark)).all()
        return data
