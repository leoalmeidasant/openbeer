class ValidateQuantity(object):

    def process(self, domain):
        if int(domain.quantity) <= 0:
            return 'Quantidade não pode ser menor ou igual a 0'
