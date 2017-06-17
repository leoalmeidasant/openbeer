import datetime
from flask import redirect, render_template, url_for, flash
from app.models.user import User
from app.models.address import Address
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
            role='user',
            gender=kwargs['gender'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        SaveCommand.execute(user)
        address = Address(
            zip_code=kwargs['address']['zip_code'],
            street=kwargs['address']['street'],
            number=kwargs['address']['number'],
            district=kwargs['address']['district'],
            city=kwargs['address']['city'],
            user_id=user.id,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        result = SaveCommand.execute(address)
        flash(result.result)
        return redirect(url_for('login'))

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

    @staticmethod
    def new_address(**kwargs):
        address = Address(
            zip_code=kwargs['zip_code'],
            street=kwargs['street'],
            number=kwargs['number'],
            district=kwargs['district'],
            city=kwargs['city'],
            user_id=kwargs['user_id'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        result = SaveCommand.execute(address)
        return result.result
