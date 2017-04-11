from handlers.common.CommonHandler import CommonHandler

from model.Post import Post
from model.Comment import Comment
from model.Like import Like


class PostDetailsHandler(CommonHandler):
    def get(self, post_id):
        post = Post.by_id(int(post_id))

        if post:
            likes = Like.all().filter('post =', post).count()
            comments = Comment.all().filter('post =', post).order('-created')

            self.render('post.html', post=post, likes=likes, comments=comments)
        else:
            self.redirect('/blog')
