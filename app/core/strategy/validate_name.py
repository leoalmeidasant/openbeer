class ValidateName(object):
    def __init__(self):
        pass

    def process(self, domain):
        if domain.name == domain.email:
            return 'name is equal to email'
        else:
            return ''
