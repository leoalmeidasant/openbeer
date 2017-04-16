import datetime
from flask import redirect, render_template, url_for
from app.models.user import User as User
from app.controllers.command.save_command import SaveCommand
from app.controllers.command.search_command import SearchCommand
from app.controllers.command.update_command import UpdateCommand
from app.controllers.command.delete_command import DeleteCommand

class UserController(object):

    @staticmethod
    def save(**kwargs):
        user = User(
            name=kwargs['name'],
            lastname=kwargs['lastname'],
            email=kwargs['email'],
            password=kwargs['password'],
            confirm_password=kwargs['confirm_password'],
            phone=kwargs['phone'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        result = SaveCommand.execute(user)
        return redirect(url_for('index'), message=result)

    @staticmethod
    def update(**kwargs):
        user = User(
            id=kwargs['id'],
            name=kwargs['name'],
            lastname=kwargs['lastname'],
            email=kwargs['email'],
            password=kwargs['password'],
            confirm_password=kwargs['confirm_password'],
            phone=kwargs['phone'],
            updated_at=datetime.datetime.now()
        )
        result = UpdateCommand.execute(user)
        return redirect(url_for('index'), message=result)

    @staticmethod
    def delete(user_id):
        user = User()
        result = DeleteCommand.execute(user, user_id)
        return render_template('index.html', message=result)

    @staticmethod
    def search(user_id=None):
        user = User()
        result = SearchCommand.execute(user, user_id)
        if not user_id:
            return render_template('index.html', users=result.resut)
        return result.result
