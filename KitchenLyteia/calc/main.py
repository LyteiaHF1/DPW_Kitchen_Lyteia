'''
Lyteia Kitchen
Lab 3
3/11/14
'''
import webapp2
#gets page.py
from page import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #import page
        page = Page()



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
