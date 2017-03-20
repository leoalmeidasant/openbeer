from flask import redirect, render_template, url_for
import json

from app.models.client import Client
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand

class ClientController(object):
    def __init__(self):
        pass

    @staticmethod
    def save(**kwargs):
        client = Client()
        client.name = kwargs['name']
        client.email = kwargs['email']
        client.password = kwargs['password']
        client.username = kwargs['username']

        save_command = SaveCommand()
        result = save_command.execute(client)

        return render_template('insert.html', message=result.result)

    @staticmethod
    def update(**kwargs):
        client = Client()
        client.id = kwargs['id']
        client.name = kwargs['name']
        client.email = kwargs['email']
        client.password = kwargs['password']
        client.username = kwargs['username']

        update_command = UpdateCommand()
        result = update_command.execute(client)

        return render_template('index.html', message=result.result)

    @staticmethod
    def delete(client_id):
        client = Client()
        delete_command = DeleteCommand()
        result = delete_command.execute(client, client_id)
        return render_template('index.html', message=result.result)


    @staticmethod
    def search(client_id=None):
        client = Client()
        search_command = SearchCommand()
        result = search_command.execute(client, client_id)
        if not client_id:
            return render_template('index.html', clients=result.result)
        return result.result
