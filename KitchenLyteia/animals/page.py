'''
Lyteia
Lab 4
3/13/14
'''


class Page():
    def __init__(self):

        self.__header = '''
<!DOCTYPE>
<html>
<head>
<title>Countries</title>
<link rel='stylesheet' href='css/main.css' />
</head>
<body>
<div id="container">'''
        self.__form='''
<nav>
<a href='/?animal=0'><button></button></a>
<a href='/?animal=1'><button></button></a>
<a href='/?animal=2'><button></button></a>
<a href='/?animal=3'><button></button></a>
<a href='/?animal=4'><button></button></a>
</nav>'''