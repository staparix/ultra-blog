from handlers.common.CommonHandler import CommonHandler
from model.Post import Post


class EditPostHandler(CommonHandler):
    def get(self, post_id):
        if self.is_logged():
            post = Post.by_id(int(post_id))
            if post.author.key().id() == self.user.key().id():
                self.render('write.html', post_id=post_id, post_title=post.title, post_body=post.body, edit=True)
            else:
                self.redirect('/blog')
