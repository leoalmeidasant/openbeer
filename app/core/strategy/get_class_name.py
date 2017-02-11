class GetClassName(object):
    def __init__(self):
        pass

    @staticmethod
    def name(domain):
        return type(domain).__name__
