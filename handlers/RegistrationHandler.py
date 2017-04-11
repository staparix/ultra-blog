from model.User import Users
from handlers.SignupHandler import Signup


class RegistrationHandler(Signup):
    def done(self):
        user = Users.by_name(self.username)
        if user:
            msg = 'That user already exists.'
            self.render('signup.html', error_username=msg)
        else:
            user = Users.register(self.username, self.password, self.email)
            user.put()

            self.login(user)
            self.redirect('/blog')
