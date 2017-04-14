from handlers.common.CommonHandler import CommonHandler
from model.Comment import Comment
from utils.validationDecorators import post_exists, user_logged_in


class NewCommentHandler(CommonHandler):
    @post_exists
    def new_comment(self, *args, **kwargs):
        comment = self.request.get('comment').strip()
        if comment:
            post = kwargs.get('post')
            new_comment = Comment.save(author=self.user, post=post, comment=comment)
            new_comment.put()

    @user_logged_in
    def post(self):
        post_id = self.request.get('postId')
        self.new_comment(self, post_id=post_id)
        self.redirect('/blog/' + post_id)
