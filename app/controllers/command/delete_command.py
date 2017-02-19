from app.core.facade.facade import Facade

class DeleteCommand(object):
    def __init__(self):
        pass

    def execute(self, domain, client_id):
        facade = Facade()
        return facade.delete(domain, client_id)
