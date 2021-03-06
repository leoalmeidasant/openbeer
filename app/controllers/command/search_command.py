from app.core.facade.facade import Facade

class SearchCommand(object):
    def __init__(self):
        pass

    def execute(self, domain, client_id=None):
        facade = Facade()
        return facade.search(domain, client_id)
