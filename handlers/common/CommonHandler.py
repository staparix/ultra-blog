import webapp2
import jinja2
import os
from utils import hashing
from model.User import Users
import config

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(config.view_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class CommonHandler(webapp2.RequestHandler):
    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and hashing.check_secure_val(cookie_val)

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def set_secure_cookie(self, name, val):
        cookie_val = hashing.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def render_str(self, template, **params):
        t = JINJA_ENVIRONMENT.get_template(template)
        params['user'] = self.user
        return t.render(params)

    def render(self, template, **kw):
        self.response.out.write(self.render_str(template, **kw))

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def is_logged(self):
        if not self.user:
            self.redirect('/login')
            return False
        else:
            return True

    def initialize(self, *a, **kw):

        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and Users.by_id(int(uid))
