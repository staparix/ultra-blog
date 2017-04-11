import webapp2


class Main(webapp2.RequestHandler):
    def get(self):
        self.redirect('/blog')
