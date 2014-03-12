'''
Lyte
getters and setters 2
'''
import webapp2
#From document import Class
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.page = Page() #triggers __init__ function in page Class
        self.page.title = "Contact Us"
        self.response.write(self.page.all)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


#data objects
#charater class form oop review do 5 instances


