'''
Lyte
Lecture day 3
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.luke = Character()
        self.luke.name = "Luke Skywalker"
        self.luke.age = 19
        self.luke.profession = "Jedi Knight"

        self.leia = Character()
        self.leia.name = "Leia Organa"
        self.leia.profession = "Princess"
        self.leia.age = self.luke.age
        self.leia.speak()

        self.yoda = Character()
        self.yoda.name = "Master Yoda"
        self.yoda.profession = "Jedi Knight"
        self.yoda.age = 896
        self.yoda.speak()

        for y in self.yoda.__dict__: #tells what the object has list attributes
            print y


class Character(): #this is an class
    def __init__(self):
        #defult value here
        self.name = ""
        self.age = 0
        self.profession = ""

    def fight(self):
        print "WAR!!!"

    def speak(self):
        print "Hey My Name Is " + self.name




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
