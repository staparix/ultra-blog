from google.appengine.ext import db
from handlers.common.CommonHandler import CommonHandler
from utils.validationDecorators import user_owns_post, post_exists, user_logged_in


class DeletePostHandler(CommonHandler):
    @post_exists
    @user_owns_post
    def delete_post(self, *args, **kwargs):
        post = kwargs.get('post')
        db.delete(post.key())

    @user_logged_in
    def post(self):
        post_id = self.request.get('postId')
        self.delete_post(self, post_id=post_id)
        self.redirect('/blog')
