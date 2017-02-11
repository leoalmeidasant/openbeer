import psycopg2
import psycopg2.extras

from app.core.dao.connection import Connection


class ClientDao(object):
    def __init__(self):
        c = Connection()
        self.conn = c.connect()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def save(self, domain):
        self.cur.execute('INSERT INTO clients (name, email) VALUES (%s, %s) RETURNING id', (domain.name, domain.email))
        id = self.cur.fetchone()[0]
        if not id:
            return 'Error to insert in table clients'
        self.conn.commit()
        return 'Successfully insert in table clients'
