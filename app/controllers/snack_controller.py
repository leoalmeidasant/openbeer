import datetime
from flask import redirect, render_template, url_for
from app import db
from app.models.snack import Snack
from app.core.strategy.upload_image import UploadImage
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand

class SnackController(object):

    @staticmethod
    def save(**kwargs):
        snack = Snack(
            name=kwargs['name'],
            description=kwargs['description'],
            value=kwargs['value'],
            type=kwargs['type'],
            quantity=kwargs['quantity'],
            image=kwargs['image'].filename,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        upload = UploadImage()
        upload.process(kwargs)
        result = SaveCommand.execute(snack)
        return redirect(url_for('new_snack', message=result.result))

    @staticmethod
    def update(**kwargs):
        snack = Snack(
            id=kwargs['id'],
            name=kwargs['name'],
            description=kwargs['description'],
            value=kwargs['value'],
            type=kwargs['type'],
            quantity=kwargs['quantity'],
            updated_at=datetime.datetime.now()
        )
        result = UpdateCommand.execute(snack)
        return redirect(url_for('edit_snack', id=kwargs['id'], message=result.result))

    @staticmethod
    def delete(snack_id):
        snack = Snack()
        result = DeleteCommand.execute(snack, snack_id)
        return redirect(url_for('snack', message=result.result))

    @staticmethod
    def search(snack_id=None):
        snack = Snack()
        result = SearchCommand.execute(snack, snack_id)
        return result.result
