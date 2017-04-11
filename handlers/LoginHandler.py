from handlers.common.CommonHandler import CommonHandler
from model.User import Users


class LoginHandler(CommonHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = Users.login(username, password)

        if u:
            self.login(u)
            self.redirect('/blog')

        else:
            msg = 'Invalid login'
            self.render('login.html', error=msg)
