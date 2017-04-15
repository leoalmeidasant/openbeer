from app.models.user import User

class Admin(User):
    def __init__(self):
        super().__init__()
        self.__name = None

    @property
    def name(self):
        return self.__name

    @setter.name
    def name(self, name):
        self.__name = name
        
