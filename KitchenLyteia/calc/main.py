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

          #nikeFoampositeOne Shoe Instance

        nfo = Shoe()
        nfo.name = 'Nike Foamposite One'
        nfo.price = 220 #$
        nfo.limit = 1 #pairs
        nfo.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"

        #lebron Shoe Instance

        leb = Shoe()
        leb.name = 'LeBrons'
        leb.price = 200 #$
        leb.limit = 1 #pairs
        leb.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"


        #kobe Shoe Instance

        kobe = Shoe()
        kobe.name = 'Kobes'
        kobe.price = 120 #$
        kobe.limit = 4 #pairs
        kobe.img ="http://upload.wikimedia.org/wikipedia/en/3/37/Jumpman_logo.svg"



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
