from app.core.dao.client_dao import ClientDao
from app.core.result.result import Result
from app.core.strategy.validate_name import ValidateName
from app.core.strategy.get_class_name import GetClassName

class Facade(object):
    def __init__(self):
        self.__map_daos = {}
        self.__map_business_rules = {}

        #create instances of DAO classes
        client_dao = ClientDao()

        #adding each dao in map indexing by class name
        self.__map_daos['Client'] = client_dao

        #creating instances of busisness rules to be used
        validate_name = ValidateName()

        #lists of rules to validate crud
        rules_save_client = []

        #adding rules to array
        rules_save_client.append(validate_name)

        #map to agroup rules
        map_rules_client = {}

        map_rules_client['SAVE'] = rules_save_client

        self.__map_business_rules['Client'] = map_rules_client

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
