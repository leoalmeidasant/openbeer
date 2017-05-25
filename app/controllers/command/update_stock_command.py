from app.core.facade.facade import Facade

class UpdateStockCommand(object):
    def __init__(self):
        pass

    @staticmethod
    def execute(domain):
        facade = Facade()
        return facade.update_stock(domain)
