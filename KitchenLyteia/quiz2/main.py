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



class Jordan(Sneaker):
    def __init__(self):
        self.sport = "Basketball"
