from handlers.common.CommonHandler import CommonHandler
from model.Post import Post


class NewPostHandler(CommonHandler):
    def get(self):
        self.render("write.html")

    def post(self):
        if self.is_logged():
            title = self.request.get('postTitle').strip()
            body = self.request.get('postBody').strip()
            post_id = self.request.get('postId')

            if not title or not body:
                self.render('write.html', post_title=title, post_body=body, error=True)
            else:
                # if post_id exist it means post is already created and we should update entity
                if post_id:
                    post = Post.by_id(int(post_id))
                    post.title = title
                    post.body = body
                    post.put()
                    self.redirect('/blog/' + post_id)
                else:
                    post = Post.save(title=title, body=body, author=self.user)
                    post.put()
                    self.redirect('/blog/' + str(post.key().id()))
