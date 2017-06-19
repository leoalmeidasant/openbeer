class ValidateValue(object):

    def process(self, domain):
        if int(domain.value) <= 0:
            return 'Valor não pode ser menor ou igual a 0'
