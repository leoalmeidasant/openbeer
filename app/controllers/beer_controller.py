import datetime
from flask import redirect, render_template, url_for, flash
from app import db
from app.models.beer import Beer
from app.core.strategy.upload_image import UploadImage
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand

class BeerController(object):

    @staticmethod
    def save(**kwargs):
        beer = Beer(
            name=kwargs['name'],
            description=kwargs['description'],
            value=kwargs['value'],
            type=kwargs['type'],
            mark=kwargs['mark'],
            quantity=kwargs['quantity'],
            image=kwargs['image'].filename,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        upload = UploadImage()
        upload.process(kwargs)
        result = SaveCommand.execute(beer)
        return redirect(url_for('new_beer', message=result.result))

    @staticmethod
    def update(**kwargs):
        beer = Beer(
            id=kwargs['id'],
            name=kwargs['name'],
            description=kwargs['description'],
            value=kwargs['value'],
            mark=kwargs['mark'],
            type=kwargs['type'],
            quantity=kwargs['quantity'],
            updated_at=datetime.datetime.now()
        )
        result = UpdateCommand.execute(beer)
        flash(result.result)
        return redirect(url_for('beer'))

    @staticmethod
    def delete(beer_id):
        beer = Beer()
        result = DeleteCommand.execute(beer, beer_id)
        return redirect(url_for('beer', message=result.result))

    @staticmethod
    def search(beer_id=None):
        beer = Beer()
        result = SearchCommand.execute(beer, beer_id)
        # import ipdb; ipdb.set_trace()
        return result.result
