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
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1> Hello CSSI </h1> <p>Hello, World!</p>')

class memeGenerator(webapp2.RequestHandler):
    def get(self): #the get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        the_variable_dict = {
                "line1": "If Cinderella's shoe was a perfect fit",
                "line2": "Why did it fall off?",
                "img_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
                }
        self.response.write(welcome_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps root url to MainPage class
    ('/mg', memeGenerator),
    ], debug=True)
