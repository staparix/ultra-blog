from google.appengine.ext import db
from handlers.common.CommonHandler import CommonHandler
from model.Post import Post
from model.Like import Like


class LikeHandler(CommonHandler):
    def post(self):
        if self.is_logged():
            post_id = self.request.get('postId')
            post = Post.by_id(int(post_id))

            if post.author.key().id() != self.user.key().id():
                exists = Like.all().filter('post =', post).filter('user', self.user).get()
                if exists:
                    db.delete(exists)
                else:
                    new_like = Like(user=self.user, post=post)
                    new_like.put()

            self.redirect('/blog/' + post_id)
