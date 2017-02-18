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

    def search(self, client_id=None):
        if client_id:
            self.cur.execute('SELECT * FROM clients WHERE id=%s' % client_id)
            result = self.cur.fetchone()
            client = dict(result)
            return client
        else:
            self.cur.execute('SELECT * FROM clients')
            result = self.cur.fetchall()
            clients = []
            for row in result:
                clients.append(dict(row))
            if not clients:
                return "We don't have clients yet"
            return clients
