'''
Lyte
Day 3 Lecture
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.t = Transcripts()
        self.t.grade1 = 90
        self.t.grade2 = 100
        self.t.quiz1 = 75
        self.t.quiz2 = 99
        self.t.calc_grade()
        self.t.final_grade +=5
        print self.t.final_grade

        #self. makes it asscesable it an attribute so its not just local to the function

class Transcripts(object):#the "object" inheritance is important for new style if dont put will think its doing the old syle
    def __init__(self):
        self.grade1 = 0
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.__final_grade = 0 #private property

        #_protected
        #__private
        #public

    #make final grade a property
    @property
    def final_grade(self):#THIS ALLOWS READ ACCESS
        return self.__final_grade

    #name of getter function + .setter
    @final_grade.setter #THIS ALLOWS WRITE ACCESS
    def final_grade(self, grade):
        self.__final_grade = grade


    def calc_grade(self):
        avg = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2)/4
        self.__final_grade = avg




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
