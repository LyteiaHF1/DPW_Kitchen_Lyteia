'''
Lyteia
DPW Final
March 27,2014
'''
import urllib2#import for xml
from xml.dom import minidom#import for minidom

class Model(object):
	def __init__(self):
		self.__url = "http://rebeccacarroll.com/api/music/music.xml"#where the api is
		self.__request = urllib2.Request(self.__url)#request
		self.__opener = urllib2.build_opener()#opener
		self.__result = self.__opener.open(self.__request)#result
		self.__xmldoc = minidom.parse(self.__result)#parse xml
		self.__songs = self.__xmldoc.getElementsByTagName('track')#get element by tag
		self.__musicArray = []#empty array for songs
		self.__songNames = []#emepty array for song names
        #Loop Through
		for s in self.__songs:
			song = dict()#dictionary of songs
			song['mp3'] = s.getAttribute('file')#gets file
			song['title'] = s.getElementsByTagName('title')[0].firstChild.nodeValue#gets element by tag
			song['artist'] = s.getElementsByTagName('artist')[0].firstChild.nodeValue#gets element by tag
			song['length'] = s.getElementsByTagName('length')[0].firstChild.nodeValue#gets element by tag
			song['year'] = s.getElementsByTagName('year')[0].firstChild.nodeValue#gets element by tag
			song['label'] = s.getElementsByTagName('label')[0].firstChild.nodeValue#gets element by tag
			song['cover'] = s.getElementsByTagName('cover')[0].firstChild.nodeValue#gets element by tag
			self.__musicArray.append(song)
			self.__songNames.append(song['title'])
	@property
	def names(self):
		return self.__songNames

class Page(object):
	def __init__(self):
		self.__head = '''
<!DOCTYPE>
<html>
	<head>
		<title>Top 10 Pop Songs</title>
	</head>
<body>
		'''
		self.__nav = '''
	<nav>
		<ul>'''
		self.__body = '''
		'''
		self.__close = '''
</body>
</html>
		'''
	@property
	def header(self):
		return self.__head

	@property
	def body(self):
		return self.__body
	@body.setter
	def body(self,b):
		self.__body = b

	@property
	def close(self):
		return self.__close

	@property
	def nav(self):
		return self.__nav

	@nav.setter
	def nav(self,li):
		for i in li:
			self.__nav + '<li><a href="/?song='+i+'">'+i+'</a></li>'
		self.__nav = self.__nav + '</ul></nav>'

class Songs(object):#class for what we see
	def __init__(self):
		self.__view = ''


	@property
	def view(self):
		return self.__view
