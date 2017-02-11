from app.models.domain import Domain

class Client(Domain):
    def __init__(self):
        self.__name = None
        self.__email = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
