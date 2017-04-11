from handlers.common.CommonHandler import CommonHandler
from model.Post import Post


class BlogFrontHandler(CommonHandler):
    def get(self):
        posts = Post.all().order('-created')
        self.render("home.html", posts=posts)
