import psycopg2
import psycopg2.extras

from app.core.dao.connection import Connection
from app.models.product import Product

class ProductDao(object):
    def __init__(self):
        c = Connection()
        self.conn = c.connect()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def save(self, domain):
        self.cur.execute('INSERT INTO products (name, description, price, amount, category, type, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id', (domain.name, domain.description, domain.price, domain.amount, domain.category, domain.type, domain.created_at, domain.updated_at))
        id = self.cur.fetchone()[0]
        if not id:
            return 'Error to insert in table products'
        self.conn.commit()
        return 'Succesfully inser in table producst'

    def update(self, domain):
        try:
            self.cur.execute('UPDATE producst SET name=(%s), description=(%s), price=(%s), amount=(%s), category=(%s), type=(%s), updated_at=(%s) WHERE id=(%s)', (domain.name, domain.description, domain.price, domain.amount, domain.category, domain.type, domain.updated_at))
            self.conn.commit()
            return 'Update success!'
        except:
            return 'Not able to update client'

    def delete(self, product_id):
        try:
            self.cur.execute('DELETE FROM products WHERE id=(%s)' % product_id)
            self.conn.commit()
            return 'Success!'
        except:
            return 'Not able to delete client'


    def search(self, product_id=None):
        if product_id:
            self.cur.execute('SELECT * FROM products WHERE id=%s' % product_id)
            result = self.cur.fetchone()
            product = dict(result)
            return product
        else:
            self.cur.execute('SELECT * FROM CLIENTS ORDER BY id ASC')
            result = self.cur.fetchall()
            products = []
            for row in result:
                products.append(dict(row))
            if not products:
                return "We don't have products"
            return products
