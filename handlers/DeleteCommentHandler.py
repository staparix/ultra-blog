from google.appengine.ext import db
from model.Comment import Comment
from handlers.common.CommonHandler import CommonHandler


class DeleteCommentHandler(CommonHandler):
    def post(self):
        if self.is_logged():
            comment_id = self.request.get('commentId')
            post_id = self.request.get('postId')
            comment = Comment.by_id(int(comment_id))

            if comment and comment.comment_author.key().id() == self.user.key().id():
                db.delete(comment.key())
                self.redirect('/blog/' + post_id)
