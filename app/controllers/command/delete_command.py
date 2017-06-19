from app.core.facade.facade import Facade

class DeleteCommand(object):
    def __init__(self):
        pass

    @staticmethod
    def execute(domain, id):
        facade = Facade()
        return facade.delete(domain, id)
