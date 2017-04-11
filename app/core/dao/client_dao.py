import psycopg2
import psycopg2.extras

from app.core.dao.connection import Connection
from app.models.client import Client


class ClientDao(object):
    def __init__(self):
        c = Connection()
        self.conn = c.connect()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def save(self, domain):
        self.cur.execute('INSERT INTO clients (name, lastname, email, password, confirm_password, phone, created_at, updated_at) VALUES (%s, %s) RETURNING id', (domain.name, domain.lastname, domain.email, domain.password, domain.confirm_password, domain.phone, domain.created_at, domain.updated_at))
        id = self.cur.fetchone()[0]
        if not id:
            return 'Error to insert in table clients'
        self.conn.commit()
        return 'Successfully insert in table clients'

    def update(self, domain):
        try:
            self.cur.execute('UPDATE clients SET name=(%s), lastname=(%s), email=(%s), password=(%s), confirm_password=(%s), phone(%s), updated_at=(%s) WHERE id=(%s)', (domain.name, domain.lastname, domain.email, domain.password, domain.confirm_password, domain.phone, domain.updated_at, domain.id))
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

    def validate_login(self, email):
        self.cur.execute("SELECT * FROM clients where email=('%s')" % email)
        result = self.cur.fetchone()
        if result:
            client = Client()
            client.id = result['id']
            client.name = result['name']
            client.password = result['password']
            client.email = result['email']
            client.username = result['username']
            return client
        else:
            return result
