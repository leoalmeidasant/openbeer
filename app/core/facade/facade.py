from app.core.dao.user_dao import UserDao
from app.core.dao.beer_dao import BeerDao
from app.core.dao.address_dao import AddressDao
from app.core.result.result import Result
from app.core.strategy.validate_name import ValidateName
from app.core.strategy.get_class_name import GetClassName

class Facade(object):
    def __init__(self):
        self.__map_daos = {}
        self.__map_business_rules = {}

        #create instances of DAO classes
        user_dao = UserDao()
        beer_dao = BeerDao()
        address_dao = AddressDao()

        #adding each dao in map indexing by class name
        self.__map_daos['User'] = user_dao
        self.__map_daos['Beer'] = beer_dao
        self.__map_daos['Address'] = address_dao

        #creating instances of busisness rules to be used
        validate_name = ValidateName()

        #lists of rules to validate crud of user
        rules_save_user = []
        rules_search_user = []
        rules_update_user = []
        rules_delete_user = []

        #list of rules to validate crud of address
        rules_save_address = []
        rules_search_address = []
        rules_update_address = []
        rules_delete_address = []

        #list of rules to validate crud of beer
        rules_save_beer = []
        rules_search_beer = []
        rules_update_beer = []
        rules_delete_beer = []

        #adding rules to array
        # rules_save_user.append(validate_name)

        #map to agroup rules
        map_rules_user = {}
        map_rules_beer = {}
        map_rules_address = {}

        #adding rules to maps
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

        self.__map_business_rules['User'] = map_rules_user
        self.__map_business_rules['Beer'] = map_rules_beer
        self.__map_business_rules['Address'] = map_rules_address

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
