'''
Lyteia
Quiz 2
3/13/14
'''
#sneakers class
class Sneaker(object):
    def __init__(self):
        #type of sneaker
        self.__type  = "Retro or Heat"
        #type of sport
        self.__sport = "Basketball or Running"
        #type of brand
        self.__brand = "Jordan,Lebron,Kobe"

        #getter
        @property
        def heat(self):
            return "these are HEAT"

        #getter for sport
        @property
        def sport(self):
            return self.__sport


        #setter for sport
        @sport.setter
        def sport(self, v):
            self.__sport = v


#Jordan class an instance of a sneaker
class Jordan(Sneaker):
    def __init__(self):
        self.sport = "Basketball"
        self.heat = "Retro"
        self.__cost = "$"

        #getter for cost
        @property
        def cost(self):
          return self.__cost

        #setter for cost
        @cost.setter
        def cost(self, p):
            return self.__cost = p

sneaker = Jordan()
sneaker.cost = "$400"

print "My New Js Ran Me" +sneaker.cost+ " ,But They Are  "+sneaker.heat+" And They Are For "+sneaker.sport+"!  Even Though I May Never Wear Them For That Its Still GREAT :)"



