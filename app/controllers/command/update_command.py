from app.core.facade.facade import Facade

class UpdateCommand(object):
    def __init__(self):
        pass

    @staticmethod
    def execute(self, domain):
        facade = Facade()
        return facade.update(domain)
