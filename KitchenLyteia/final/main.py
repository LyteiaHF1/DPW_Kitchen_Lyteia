'''
Lyteia
DPW Final
March 27,2014
'''
import webapp2
import urllib2#imoprt for xml
from xml.dom import minidom#import for minidom
class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
