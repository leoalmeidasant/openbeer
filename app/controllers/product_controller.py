import json
from flask import redirect, render_template, url_for
from app.models.product import Product
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand

class ProductController(object):
    def __init__(self):
        pass

    def save(**kwargs):
        product = Product()
        product.name = kwargs['name']
        product.description = kwargs['description']
        product.price = kwargs['price']
        product.amount = kwargs['amount']
        product.category = kwargs['category']
        product.type = kwargs['type']

        result = SaveCommand.execute(product)
        return 200 #temporario

    def update(**kwargs):
        product = Product()
        product.id = kwargs['id']
        product.name = kwargs['name']
        product.description = kwargs['description']
        product.price = kwargs['price']
        product.amount = kwargs['amount']
        product.category = kwargs['category']
        product.type = kwargs['type']

        result = UpdateCommand.execute(product)
        return 200 #temporario

    def delete(product_id):
        product = Product()
        result = DeleteCommand.execute(product, product_id)
        return 200

    def search(product_id=None):
        product = Product()
        result = SearchCommand.execute(product, product_id)
        if not product_id:
            return 200 #renderiza todos
        return result.result
