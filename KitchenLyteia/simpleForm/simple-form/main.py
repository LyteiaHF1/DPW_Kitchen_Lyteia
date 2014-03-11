'''
Lyteia Kitchen
3/6/2014
Lecture Day 2
'''
import webapp2 #importing additional code handles going to a browser
from page import Page

#Master Class (Where it begins)
class MainHandler(webapp2.RequestHandler):

#unique to framework
#this function runs 1st catalyst

    def get(self):
    #start writing code
        if self.request.GET:
            info = self.request.GET['first_name'] + ' ' self.request.GET['last_name']
            page = Page(self)#creates page objects
            self.response.write(page.print_contents(info))
        else:
            page = Page(self)
            self.response.write(page.print_contents())

#associates class with framework
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
