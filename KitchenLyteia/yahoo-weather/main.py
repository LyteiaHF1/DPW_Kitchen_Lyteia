#Lyteia
#Day5 Lecture
#March 18,2014

import webapp2
import xml.etree.ElementTree as ET #libary for working with xml in python

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        page.inputs = {'zip': 'text', 'Submit': 'submit'}
        page.create_inputs()
        self.response.write(page.print_out("Enter your zip"))

        if self.request.GET:#if there is info in the url
            zip = self.request.GET['zip']
            url = "http://xml.weather.yahoo.com/forecastrss?p=" #where the API is
            #step 1 assemble request
            request = urllib2.Request(url + zip)#assembles request
            #2 use url lib2 to create an object to get the url
            opener = urllib2.build_opener()
            #3 use url to get result-request info from API
            result = opener.open(request)
            #print result
            #4 parse the result
            xmldoc = ET.parse(result)
            root = xmldoc.getroot()
            print root.tag
            self.response.write(root[0][0].text)
            list = root[0].findall('item')
            print item

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
