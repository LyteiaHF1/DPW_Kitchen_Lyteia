
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        fp = FormPage()
        #pass info into what i want in form
        fp.inputs = {"first_name": "text", "last_name": "text", "Submit":"submit"}
        fp.create_inputs()
        self.response.write(fp.print_out())



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

     def print_out(self):
        return self._head + self.__form_open + self.__input_string + self.__form_close + self._close

     @property
     def inputs(self):
        pass

     @inputs.setter
     def inputs(self, dict):
        self.__inputs = dict

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
