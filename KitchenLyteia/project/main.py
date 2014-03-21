'''
Lyteia
3/18/14
API Project(Youtube/Viemo)
'''
import webapp2
import urllib2
from xml.dom import minidom
class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        page.inputs = {'search':'text', 'Submit': 'submit'}
        page.create_inputs()
        self.response.write(page.print_out("Search Artist"))

        if self.request.GET:

            search = self.request.GET['search']

            url = "http://vimeo.com/api/v2/video/video_id.xml"
            request = urllib2.Request(url+search)

            opener = urllib2.build_opener()
            result = opener.open(request)
            xmldoc = minidom.parse(request)

            self.response.write(xmldoc.getElemetsByTagName('videos')[0].firstChild.nodeValue)
            content = '<br />'
            list = xmldoc.getElementsByTagName('video')
            for l in list:
                content += l.attributes['title'].value

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
