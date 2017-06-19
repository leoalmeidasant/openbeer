import random

class CalculateFare(object):

    @staticmethod
    def calculate(city):
        fare = float(random.randint(5, len(city.lower())))
        return fare
