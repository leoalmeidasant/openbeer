import re

class ValidateEmail(object):

    def process(self, domain):
        if not re.match(r"[^@|\s]+@[^@]+\.[^@|\s]+", domain.email):
            return 'Email não é valido'
