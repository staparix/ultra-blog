from handlers.common.CommonHandler import CommonHandler
from utils import authValidation


class Signup(CommonHandler):
    def get(self):
        self.render('signup.html')

    def post(self):

        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')
        params = dict(username=self.username, email=self.email)

        if not authValidation.valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not authValidation.valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True

        if self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not authValidation.valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError
