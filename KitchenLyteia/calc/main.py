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

        #airJordan Shoe Instance

        airj = Shoe()
        airj.name = 'Air Jordans'
        airj.price = 180 #$
        airj.limit = 2 #pairs
        airj.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        #nikeFoampositePro Shoe Instance

        nfp = Shoe()
        nfp.name = 'Nike Foamposite Pro'
        nfp.price = 220 #$
        nfp.limit = 1 #pairs
        nfp.img = "http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"


 #Objects
class Shoe(object):
    def __init__(self):
        self.name = ''
        self.__price = 0
        self.__limit = 0
        self.img = ''





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
