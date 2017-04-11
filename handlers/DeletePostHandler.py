from google.appengine.ext import db
from handlers.common.CommonHandler import CommonHandler
from model.Post import Post


class DeletePostHandler(CommonHandler):
    def post(self):
        if self.is_logged():
            post_id = self.request.get('postId')
            post = Post.by_id(int(post_id))
            if post.author.key().id() == self.user.key().id():
                db.delete(post.key())
            self.redirect('/blog')
