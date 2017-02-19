import psycopg2
import os
from urllib.parse import urlparse

class Connection(object):
    def __init__(self):
        # self.host = os.environ['DB_HOST']
        # self.user = os.environ['DB_USER']
        # self.password = os.environ['DB_PASS']
        # self.dbname = os.environ['DB_NAME']
        # urlparse.uses_netloc.append('postgres')
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
        # try:
        #     conn = psycopg2.connect(host=self.host,
        #             user=self.user,
        #             password=self.password,
        #             dbname=self.dbname
        #         )
        #     print('connected with postgresql database')
        #     return conn
        # except:
        #     raise ConnectionError('not able to connection with database')


class ConnectionError(Exception):
    def __init__(self, message):
        self.message = message
