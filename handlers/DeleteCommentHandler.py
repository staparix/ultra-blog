from google.appengine.ext import db
from handlers.common.CommonHandler import CommonHandler
from utils.validationDecorators import user_owns_comment, comment_exists, user_logged_in


class DeleteCommentHandler(CommonHandler):
    @comment_exists
    @user_owns_comment
    def delete_comment(self, *args, **kwargs):
        comment = kwargs.get('comment')
        db.delete(comment.key())

    @user_logged_in
    def post(self):
        comment_id = self.request.get('commentId')
        post_id = self.request.get('postId')

        self.delete_comment(self, comment_id=comment_id)
        self.redirect('/blog/' + post_id)
