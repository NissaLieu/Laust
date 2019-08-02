#main.py This is for GAE gcloud service.
#import section Imports should always be at the top of the code...

import webapp2
import jinja2
import os

#establishes a jinja environment
the_jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

#handlers section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        webpage = the_jinja_env.get_template('templates/main.html')
        self.response.write(webpage.render())
       
class ShowMeIt(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps root url to MainPage class
    ('/results', ShowMeIt) #this maps root url to a results page after user enters input    
    ], debug=True)
