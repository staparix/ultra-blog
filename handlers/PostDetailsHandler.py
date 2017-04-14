from handlers.common.CommonHandler import CommonHandler

from model.Comment import Comment
from model.Like import Like
from utils.validationDecorators import post_exists


class PostDetailsHandler(CommonHandler):

    @post_exists
    def post_details(self, *args, **kwargs):
        post = kwargs.get('post')
        likes = Like.all().filter('post =', post).count()
        comments = Comment.all().filter('post =', post).order('-created')
        self.render('post.html', post=post, likes=likes, comments=comments)

    def get(self, post_id):
        self.post_details(self, post_id=post_id)
