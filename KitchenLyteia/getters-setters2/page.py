'''
Lyte
getters and setters 2
'''
class Page(object):
    def __init__(self):
        self.head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
    </head>
<body>
'''
        self.body = ""
        #self.body = '''
#<a href ='?fruit=starwberry'>Strawberry</a>
#<a href = "?fruit=peach">Peach</a>
#<a href = "?fruit=orange">Orange</a>
#'''
        self.close = '''
</body>
</html>'''
        self.all = self.head+self.body+self.close #self.update_page()
        self.__title = "Welcome"

    def update_page(self):
        self.all = self.head+self.body+self.close


     #make property
    @property
    def title(self):
        return self.__title

     #make setter
    @title.setter
    def title(self, t):
        self.__title = t
        #reformat the self.all string
        self.all = self.all.format(**locals())

