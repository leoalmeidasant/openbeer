class Result(object):
    def __init__(self):
        self.__result = None

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result
