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
		page.inputs = {'movie':'text', 'submit':'submit'}
		page.create_inputs()
		self.response.write(page.print_out("Enter Movie Title"))

		if self.request.GET:
			movie = self.request.GET['movie']
			url = "http://www.omdbapi.com/?i="
			#request = urllib2.Request(url + movie)#assembles request
			request = urllib2.Request('http://www.omdbapi.com/?i=&t='+movie+'&r=XML')#use urllib2 to create an object to get the url
			opener = urllib2.build_opener()#use url lib2 to create an object to get the url
			result = opener.open(request)#use url to get result-request info from API
            #print result
            #4 parse the result
			xmldoc = minidom.parse(result)
			content = '<br/>'
			list = xmldoc.getElementsByTagName('movie')
			for l in list:
				content += '<br/>Released:  '+l.attributes['released'].value
				content += '<br/>Rated:  '+ l.attributes['rated'].value
				content += '<br/>Genre:  '+ l.attributes['genre'].value
				content += '<br/>Runtime:  '+ l.attributes['runtime'].value
				content += '<br/>Actors:  '+ l.attributes['actors'].value
				content += '<br/>Director:  '+ l.attributes['director'].value
				content += '<br/>Plot:  '+ l.attributes['plot'].value
				content +='<br/><img src="'+ l.attributes['poster'].value+'"/>'
			self.response.write(content)


class Page(object):
	def __init__(self):
		self._head = '''
<!DOCTYPE>
<html>
    <head>
      <title>Movie Search API</title>
      <link rel="stylesheet" href="css/skeleton.css">
	  <link rel="stylesheet" href="css/main.css">
    </head>
  <body>
			<h3>Search Movie Titles</h3>
		'''
		self._body = '''
        <div id='cta'>
		<p>Search Your Favorite Movies Here....Never Forget Your Fav Movie Titles And Info AGAIN!</p>
	</div>
	'''
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

	def print_out(self,msg):
		return self._head+ msg + self.__form_open + self.__input_string + self.__form_close +self._close

	@property
	def inputs(self):
		pass
	@inputs.setter
	def inputs(self, value):
		self.__inputs = value

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
