from handlers.common.CommonHandler import CommonHandler
from model.Post import Post
from model.Comment import Comment


class NewCommentHandler(CommonHandler):
    def post(self):
        if self.is_logged():
            comment = self.request.get('comment').strip()
            post_id = self.request.get('postId')
            post = Post.by_id(int(post_id))

            if comment:
                new_comment = Comment.save(author=self.user, post=post, comment=comment)
                new_comment.put()
                self.redirect('/blog/' + post_id)
            else:
                self.redirect('/blog/' + post_id)
