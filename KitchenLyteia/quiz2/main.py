'''
Lyteia
Quiz 2
3/13/14
'''
#sneakers class
class Sneaker(object):
    def __init__(self):
        self.__type  = "Retro or Heat"
        self.__sport = "Basketball or Running"
        self.__brand = "Jordan,Lebron,Kobe"

        #getter
        @property
        def heat(self):
            return "these are HEAT"
        #getter
        @property
        def sport(self):
            return self.__sport
        #setter for cost
        @sport.setter
        def cost(self, v):
            self.__sport = v



class Jordan(Sneaker):
    def __init__(self):
        self.sport = "Basketball"
