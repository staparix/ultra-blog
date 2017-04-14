from handlers.common.CommonHandler import CommonHandler
from model.Post import Post
from model.Comment import Comment
from utils.validationDecorators import comment_exists, user_owns_comment, user_logged_in


class EditCommentHandler(CommonHandler):
    @comment_exists
    @user_owns_comment
    def edit_comment(self, post_id, *args, **kwargs):
        comment = kwargs.get('comment')
        self.render('edit-comment.html', comment=comment, post_id=post_id)

    @comment_exists
    @user_owns_comment
    def save_comment(self, *args, **kwargs):
        comment = self.request.get('comment')
        old_comment = kwargs.get('comment')
        old_comment.comment = comment
        old_comment.put()

    @user_logged_in
    def get(self, post_id, comment_id):
        self.edit_comment(self, post_id=post_id, comment_id=comment_id)

    @user_logged_in
    def post(self, post_id, comment_id):
        self.save_comment(self, comment_id=comment_id)
        self.redirect('/blog/' + post_id)
