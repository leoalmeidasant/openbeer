from app.models.domain import Domain

class Products(Domain):
    def __init__(self):
        super().__init__()
        self.__name = None
        self.__description = None
        self.__price = None
        self.__amount = None
        self.__category = None
        self.__type = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type
