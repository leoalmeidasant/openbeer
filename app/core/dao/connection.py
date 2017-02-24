import psycopg2
import os
from urllib.parse import urlparse

class Connection(object):
    def __init__(self):
        self.url = urlparse(os.environ['DATABASE_URL'])

    def connect(self):
        try:
            conn = psycopg2.connect(
                database=self.url.path[1:],
                user=self.url.username,
                password=self.url.password,
                host=self.url.hostname,
                port=self.url.port
            )
            print('connected with postgresql database')
            return conn
        except:
            raise ConnectionError('not able to connect with database')

class ConnectionError(Exception):
    def __init__(self, message):
        self.message = message
