'''
Lyteia
Quiz 3
3/20/14
'''
class Sneaker():
    def __init__(self):
        self.__ryear = '2012'
        self._type = 'Jordan'
        self.__color = 'Black'

        self.Color()

    @property
    def Year(self):
        return self.__ryear

    @property
    def Color(self):
        return self.__color

    def Color():
        self.__color = 'Blue'

class Jordan(Sneaker):
    def __init__(self):
        super(Jordan, self).__init__()

        self.__ryear = '1994'
        self._type = 'Jordan'
        self.__style = 'Retro 11'
        self.condition = 'Very Near Deadstock'



class Lebron(Sneaker):
    def __init__(self):
        super(Lebron, self).__init__()

        self.__ryear = '2014'
        self._type = 'Lebron'
        self.__style = 'Elite X'
        self.condition = 'Deadstock'

