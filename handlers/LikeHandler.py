from google.appengine.ext import db
from handlers.common.CommonHandler import CommonHandler
from model.Like import Like
from utils.validationDecorators import user_logged_in, post_exists


class LikeHandler(CommonHandler):
    @post_exists
    def like_post(self, *args, **kwargs):
        post = kwargs.get('post')
        if post.author.key().id() != self.user.key().id():
            exists = Like.all().filter('post =', post).filter('user', self.user).get()
            if exists:
                db.delete(exists)
            else:
                new_like = Like(user=self.user, post=post)
                new_like.put()

    @user_logged_in
    def post(self):
        post_id = self.request.get('postId')
        self.like_post(self, post_id=post_id)
        self.redirect('/blog/' + post_id)
