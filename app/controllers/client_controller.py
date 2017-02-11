from flask import make_response
import json

from app.models.client import Client
from app.controllers.command.save_command import SaveCommand

class ClientController(object):
    def __init__(self):
        pass

    @staticmethod
    def save(**kwargs):
        client = Client()
        client.name = kwargs['name']
        client.email = kwargs['email']

        save_command = SaveCommand()
        save_command.execute(client)

        return json.dumps(kwargs)
