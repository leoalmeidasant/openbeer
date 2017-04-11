class Domain(object):
    def __init__(self):
        self.__id = None
        self.__created_at = None
        self.__updated_at = None

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at
