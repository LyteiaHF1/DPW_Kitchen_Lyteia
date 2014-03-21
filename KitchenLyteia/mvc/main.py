#Lyteia
#Day5 Lecture
#March 20,2014
#MVC

import webapp2
import urllib2 #need this for requesting info from API this step 2
from xml.dom import minidom #libary for working with xml in python

class MainHandler(webapp2.RequestHandler):
"""Main controller for my weather application
"""
    def get(self):
        page = FormPage()
        page.inputs = {'zip': 'text', 'Submit': 'submit'}
        page.create_inputs()
        self.response.write(page.print_out("Enter your zip"))

        if self.request.GET:#if there is info in the url
            zip = self.request.GET['zip']

            wm = WeatherModel(zip) #handles zip in model
            wm.send()
            wv = WeatherView()
            wv.do = wm.do
            self.response.write(wv.content)

class WeatherModel(object):
"""Handles fetching parsing and getting data from api
"""
    def __init__(self, zip):
        self.__url = 'http://xml.weather.yahoo.com/forecastrss?p='
        self.__req = urllib2.Request(self.__url + zip)#assembles request
        self.__opener = urllib2.build_opener()


    def send(self):
        self._result = self.__opener.open(self.__req)
        self.sort()

    def sort(self):
        print "sort function ran"
        #parse
        self.__xmldoc = minidom.parse(self.__result)
        self.__do = WeatherData()

        self.__do.title = xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue
        list = self.__xmldoc.getElementsByTagName('yweather:forecast')
        for l in list:
            print l.attributes['day'].value
            self.__do.code = l.attributes['code'].value
            self.__do.day = l.attributes['day'].value
            self.__do.high = l.attributes['high'].value
            self.__do.low = l.attributes['low'].value
            self.__do.condition = l.attributes['condition'].value
    @property
    def do(self):
        return self.__do

class WeatherData(object):
"""This Holds The Data Feteched By The View
"""
    def __init__(self):
        self.title = ''
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''

class WeatherView(object):
""" This Class handles how the data is shown to the user
"""
    def __init__(self):
        self.__do = WeatherData()

    def update(self):
        self.__content = '<h3>' + self.__do.title + '</h3>'
        self.__content += self.__do.day + '  :  '
        self.__content += 'HIGH:' + self.__do.high
        self.__content += 'LOW:' + self.__do.low
        self.__content += 'Condition:' + self.__do.condition + '<br />'
        print self.__content



    @property
    def do(self):
        return self.__do

    @do.setter
    def do(self,new_do):
        self.__do = new_do
        self.__do.title
        self.update()

    @property
     def content(self):
        return self.__content

class Page(object):
      def __init__(self):
        self._head ='''
<!DOCTYPE>
<html>
    <head>
        <title></title>
    </head>
  <body>
        '''
        self._body = ''
        self._close = '''
    </body>
</html>'''

class FormPage(Page):
     def __init__(self):
        #run the init function
        #super for this class run its init function
        super(FormPage, self).__init__()

        self.__form_open = '<form method="GET">'
        self.__form_close = '</form>'
        self.__inputs = dict()
        self.__input_string = ""

        #{"first_name": "text", "last_name": "text"}

     def create_inputs(self):
         for key, value in self.__inputs.iteritems():
            #print self.__inputs[i]
            #self input string for input type
            self.__input_string += '<input type="' + value+ '" name="' +key+ '" placeholder="' +key+'"/>'

     def print_out(self, msg):
        return self._head + msg + self.__form_open + self.__input_string + self.__form_close + self._close

     @property
     def inputs(self):
        pass

     @inputs.setter
     def inputs(self, dict):
        self.__inputs = dict


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
