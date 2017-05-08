from flask import session

class ItemList(object):

    @staticmethod
    def make_list():
        items = []
        for item in session['cart']['beers']:
            items.append(item)

        for item in session['cart']['snacks']:
            items.append(item)

        return items
