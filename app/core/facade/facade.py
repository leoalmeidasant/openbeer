from app.core.dao.user_dao import UserDao
from app.core.dao.beer_dao import BeerDao
from app.core.dao.snack_dao import SnackDao
from app.core.dao.address_dao import AddressDao
from app.core.dao.order_dao import OrderDao
from app.core.dao.item_dao import ItemDao
from app.core.result.result import Result
from app.core.strategy.validate_name import ValidateName
from app.core.strategy.get_class_name import GetClassName


class Facade(object):
    def __init__(self):
        self.__map_daos = {}
        self.__map_business_rules = {}

        # create instances of DAO classes
        user_dao = UserDao()
        beer_dao = BeerDao()
        address_dao = AddressDao()
        snack_dao = SnackDao()
        order_dao = OrderDao()
        item_dao = ItemDao()

        # adding each dao in map indexing by class name
        self.__map_daos['User'] = user_dao
        self.__map_daos['Beer'] = beer_dao
        self.__map_daos['Address'] = address_dao
        self.__map_daos['Snack'] = snack_dao
        self.__map_daos['Order'] = order_dao
        self.__map_daos['Item'] = item_dao

        # creating instances of busisness rules to be used
        validate_name = ValidateName()

        # lists of rules to validate crud of user
        rules_save_user = []
        rules_search_user = []
        rules_update_user = []
        rules_delete_user = []

        # list of rules to validate crud of address
        rules_save_address = []
        rules_search_address = []
        rules_update_address = []
        rules_delete_address = []

        # list of rules to validate crud of beer
        rules_save_beer = []
        rules_search_beer = []
        rules_update_beer = []
        rules_delete_beer = []

        # list of rules to validate crud of snack
        rules_save_snack = []
        rules_search_snack = []
        rules_update_snack = []
        rules_delete_snack = []

        # list of rules to validate crud of order
        rules_save_order = []
        rules_search_order = []
        rules_update_order = []
        rules_delete_order = []

        # list of rules to validate crud of item
        rules_save_item = []
        rules_search_item = []
        rules_update_item = []
        rules_delete_item = []

        #################################################

        # adding rules to array
        # rules_save_user.append(validate_name)

        # map to agroup rules
        map_rules_user = {}
        map_rules_beer = {}
        map_rules_address = {}
        map_rules_snack = {}
        map_rules_order = {}
        map_rules_item = {}

        # adding rules to maps
        map_rules_user['SAVE'] = rules_save_user
        map_rules_user['SEARCH'] = rules_search_user
        map_rules_user['UPDATE'] = rules_update_user
        map_rules_user['DELETE'] = rules_delete_user

        map_rules_beer['SAVE'] = rules_save_beer
        map_rules_beer['SEARCH'] = rules_search_beer
        map_rules_beer['UPDATE'] = rules_update_beer
        map_rules_beer['DELETE'] = rules_delete_beer

        map_rules_address['SAVE'] = rules_save_address
        map_rules_address['SEARCH'] = rules_search_address
        map_rules_address['UPDATE'] = rules_update_address
        map_rules_address['DELETE'] = rules_delete_address

        map_rules_snack['SAVE'] = rules_save_snack
        map_rules_snack['SEARCH'] = rules_search_snack
        map_rules_snack['UPDATE'] = rules_update_snack
        map_rules_snack['DELETE'] = rules_delete_snack

        map_rules_order['SAVE'] = rules_save_order
        map_rules_order['SEARCH'] = rules_search_order
        map_rules_order['UPDATE'] = rules_update_order
        map_rules_order['DELETE'] = rules_delete_order

        map_rules_item['SAVE'] = rules_save_item
        map_rules_item['SEARCH'] = rules_search_item
        map_rules_item['UPDATE'] = rules_update_item
        map_rules_item['DELETE'] = rules_delete_item

        self.__map_business_rules['User'] = map_rules_user
        self.__map_business_rules['Beer'] = map_rules_beer
        self.__map_business_rules['Address'] = map_rules_address
        self.__map_business_rules['Snack'] = map_rules_snack
        self.__map_business_rules['Order'] = map_rules_order
        self.__map_business_rules['Item'] = map_rules_item

    def save(self, domain):
        r = Result()
        class_name = GetClassName.name(domain)
        errors = self.execute_rules(domain, 'SAVE')
        if len(errors) == 0:
            dao = self.__map_daos[class_name]
            r.result = dao.save(domain)
        else:
            r.result = errors

        return r

    def search(self, domain, id=None):
        r = Result()
        class_name = GetClassName.name(domain)
        errors = self.execute_rules(domain, 'SEARCH')
        if len(errors) == 0:
            dao = self.__map_daos[class_name]
            r.result = dao.search(id)
        else:
            r.result = errors

        return r

    def update(self, domain):
        r = Result()
        class_name = GetClassName.name(domain)
        errors = self.execute_rules(domain, 'UPDATE')
        if len(errors) == 0:
            dao = self.__map_daos[class_name]
            r.result = dao.update(domain)
        else:
            r.result = errors

        return r

    def delete(self, domain, id):
        r = Result()
        class_name = GetClassName.name(domain)
        errors = self.execute_rules(domain, 'DELETE')
        if len(errors) == 0:
            dao = self.__map_daos[class_name]
            r.result = dao.delete(id)
        else:
            r.result = errors

        return r

    def execute_rules(self, domain, operation):
        class_name = GetClassName.name(domain)

        message = ''

        rules = self.__map_business_rules[class_name]

        operation_rules = rules[operation]

        for rule in operation_rules:
            if rule.process(domain):
                message += rule.process(domain) + ', '
            else:
                pass
        return message
