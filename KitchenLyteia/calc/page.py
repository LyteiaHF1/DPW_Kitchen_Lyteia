'''
Lyteia Kitchen
Lab 3
3/11/14
'''
class Page():
    def __init__(self):
        self.__header = '''
<!DOCTYPE>
<html>
    <head>
        <title>Top 5 Sneakers</title>
        <link rel="stylesheet" href="css/main.css">
    </head>
    <body>
        <div id="wrapper">
            <header>
                <h1>Top 5 Sneakers </h1>
            </header>
            <div id="main">
        '''
        self.__form = '''
            <form action="" method="GET" name="shoes" id="buttons">
                <p><a href="/?heat=1" name="heat" id="airJ">Air Jordan</a></p>
                <p><a href="/?heat=2" name="heat" id="nfp">Nike Foamposite Pro</a></p>
                <p><a href="/?heat=3" name="heat" id="nfo">Nike Foamposite One</a></p>
                <p><a href="/?heat=4" name="heat" id="leb">LeBrons</a></p>
                <p><a href="/?heat=5" name="heat" id="kobe">Kobes</a></p>
            </div>
        '''
        self.__footer = '''
            </div>
        </div>
    </body>
</html>
        '''

    def header(self):
        return self.__header

    def form(self):
        return self.__form

    def footer(self):
        return self.__footer

