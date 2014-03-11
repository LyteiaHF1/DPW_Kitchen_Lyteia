'''
Lyteia Kitchen
3/6/2014
Lab 2

'''
import webapp2
from page import Page()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Fresh By Nature"
        page = Page() #creates an instance of the page
         #p = page.open() + "Its Time To Get Fresh!" +  page.close()
        self.response.write(page.head(title))

        #if there is a URL variable then print this
        if self.request.GET:
	        gen = self.request.get("member")
	        infoString = ",".join(gen)
        	self.response.write("Thank you for your vote" + " " + self.request.GET["fName"] + " " + self.request.GET["lName"] +"(" + self.request.GET["sex"] + ")" + ", Born on " + self.request.GET["bday"] + "th" + " of " + self.request.GET["month"] + " " + self.request.GET["year"] + ". Your Top 3 Sneakers Are:" +infoString )
        else:
            self.response.write(page.registration())
        self.response.write(page.close())
        #p = p.format(**locals())
        #self.response.write(p)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
