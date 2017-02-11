class ValidateName(object):
    def __init__(self):
        pass

    def process(self, domain):
        print(domain.name + ' ' + domain.email)
        if domain.name == domain.email:
            return 'name is equal to email'
        else:
            return ''
