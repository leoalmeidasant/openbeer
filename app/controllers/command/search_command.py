from app.core.facade.facade import Facade

class SearchCommand(object):
    def __init__(self):
        pass

    @staticmethod
    def execute(domain, id=None):
        facade = Facade()
        return facade.search(domain, id)
