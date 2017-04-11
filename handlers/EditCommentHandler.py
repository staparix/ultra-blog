from handlers.common.CommonHandler import CommonHandler
from model.Post import Post
from model.Comment import Comment


class EditCommentHandler(CommonHandler):
    def get(self, post_id, comment_id):
        if self.is_logged():
            post = Post.by_id(int(post_id))
            comment = Comment.by_id(int(comment_id))
            if comment.comment_author.key().id() != self.user.key().id():
                self.redirect('/blog')

            self.render('edit-comment.html', comment=comment, post_id=post.key().id())

    def post(self, post_id, comment_id):
        if self.is_logged():
            comment = self.request.get('comment')
            old_comment = Comment.by_id(int(comment_id))

            if old_comment.comment_author.key().id() != self.user.key().id():
                self.redirect('/blog')

            old_comment.comment = comment
            old_comment.put()

            self.redirect('/blog/' + post_id)
