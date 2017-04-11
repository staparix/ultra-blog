from handlers.common.CommonHandler import CommonHandler


class LogoutHandler(CommonHandler):
    def get(self):
        self.logout()
        self.redirect('/login')
