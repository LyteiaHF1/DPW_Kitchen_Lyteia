'''
Lyteia
Quiz 3
3/20/14
'''
class Sneaker(object):
    def __init__(self):
        self.__ryear = '2012'
        self._type = 'Jordan'
        self.__color = 'Black'



class Jordan(Sneaker):
    def __init__(self):
        super(Jordan, self).__init__()

        self.__ryear = '1994'
        self._type = 'Jordan'
        self.__style = 'Retro 11'
        self.condition = 'Very Near Deadstock'

       