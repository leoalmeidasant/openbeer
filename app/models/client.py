from app.models.domain import Domain

class Client(Domain):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__username = None
        self.__email = None
        self.__password = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password


    @password.setter
    def password(self, password):
        self.__password = password
