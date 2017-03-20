import psycopg2
import psycopg2.extras

from app.core.dao.connection import Connection


class ClientDao(object):
    def __init__(self):
        c = Connection()
        self.conn = c.connect()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def save(self, domain):
        self.cur.execute('INSERT INTO clients (name, email, password, username) VALUES (%s, %s, %s, %s) RETURNING id', (domain.name, domain.email, domain.password, domain.username))
        id = self.cur.fetchone()[0]
        if not id:
            return 'Error to insert in table clients'
        self.conn.commit()
        return 'Successfully insert in table clients'

    def update(self, domain):
        try:
            self.cur.execute('UPDATE clients SET name=(%s), email=(%s), password=(%s), username=(%s) WHERE id=(%s)', (domain.name, domain.email, domain.password, domain.username, domain.id))
            self.conn.commit()
            return 'Update success!'
        except:
            return 'Not able to update client'

    def delete(self, client_id):
        try:
            self.cur.execute('DELETE FROM clients WHERE id=(%s)' % client_id)
            self.conn.commit()
            return 'Sucess!'
        except:
            return 'Not able to delete client'

    def search(self, client_id=None):
        if client_id:
            self.cur.execute('SELECT * FROM clients WHERE id=%s' % client_id)
            result = self.cur.fetchone()
            client = dict(result)
            return client
        else:
            self.cur.execute('SELECT * FROM clients ORDER BY id ASC')
            result = self.cur.fetchall()
            clients = []
            for row in result:
                clients.append(dict(row))
            if not clients:
                return "We don't have clients yet"
            return clients

    def validate_login(self, username, password):
        self.curt.execute('SELECT * FROM clients WHERE username=(%s) and password=(%s)' % username, password)
        client = dict(self.cur.fetchone())
        if not client:
            return None
        return client
