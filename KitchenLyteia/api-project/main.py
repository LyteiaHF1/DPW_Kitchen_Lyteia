'''
Lyteia
API Project
DPW
'''
import webapp2
from xml.dom import minidom
import urllib2
import json #Import Json Libary for xml

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        page.inputs = {'movie': 'text', 'Submit': 'submit'}
        page.create_inputs()
        self.response.write(page.print_out("Enter movie title"))

	if self.request.GET:#if there is info in the url
            movie = self.request.GET['movie']
            #url = "http://www.omdbapi.com/?t=" #where the API is
            #step 1 assemble request
            #request = urllib2.Request(url + movie)#assembles request
            #2 use url lib2 to create an object to get the url
            #opener = urllib2.build_opener()
            #3 use url to get result-request info from API
            #result = opener.open(request)


class SearchModel(object):
"""This Class Does All The Parsing and Getting Data From API
"""
    def __init__(self,movie):
		self.__url = 'http://www.omdbapi.com/?t='
		self.__request = urllib2.Request(self.__url+movie)
		self.__opener = urllib2.build_opener()



class Page(object):
	'''This Class Takes Care Of Basic HTML Componets
	'''
	def __init__(self):
		self._head = '''
<!DOCTYPE HTML>

	<head>
		<title>API Project</title>
	</head>
	<body>
		<h1>Search Your Fav Movies Here</h1>
		'''
		self._body = ''
		self._close = '''
		</body>
		</html>'''

	@property
	def body(self):
		pass
	@body.setter
	def body(self, value):
		self._body = value

	def print_out(self):
		return self._head +self._body +self._close


class FormPage(Page):
	def __init__(self):
		#run the intantiating function for the super class
		#super for this class, run its init function
		super(FormPage, self).__init__()
		self.__form_open = '<form method="GET">'
		self.__form_close = '</form>'
		self.__inputs = dict()
		self.__input_string = ''

	def create_inputs(self):
		for key,value in self.__inputs.iteritems():
			#print self.__inputs[i]
			self.__input_string += '<input type="' + value + '" name="'+ key +'" placeholder="'+key+'"/>'

	def print_out(self, msg):
		return self._head +msg+ self.__form_open + self.__input_string + self.__form_close +self._close

	@property
	def inputs(self):
		pass
	@inputs.setter
	def inputs(self, value):
		self.__inputs = value


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
