'''
Lyteia Kitchen
3/6/2014
Lecture Day 2
'''
class Page():
    #Methods
    #behaviors - actions STORE CODE
    def __init__(self, main_self):
        #this is the CONSTRUCTOR Function
        pass

        #Attributes
        #traits - stores data
        self.__id = 353454565 #Really Private (As Close You Can Get)
        self._author = "Rebecca"#Private access
        self.title = "welcome to the Page" #Public access
        self.head = '''<!DOCTYPE HTML>
<html>
   <head>
      <title>Simple Form</title>
      <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
     <body>
        '''
        self. body = "Hello World!"
        self.form = '''
        <form method="GET" action="">
            <input type="text" name="first_name" />
            <input type="text" name="last_name" />
            <input type="submit" value="Enter" />

        </form>
        '''
        self.ender = '''
    </body>
</html>
   '''
        main_self.response.write("WHOOHOO PYTHON IS AWESOME")


    def print_contents(self, i=''):
        if i=='':
            return self.head+self.body+self.form+self.ender
        else:
            return self.head+i+self.ender

class Button():
    def __init__(self):
        #this is the CONSTRUCTOR Function
        self.label = "Contact Me"
        self.size = 100