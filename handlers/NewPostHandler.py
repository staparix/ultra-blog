from handlers.common.CommonHandler import CommonHandler
from model.Post import Post
from utils.validationDecorators import user_logged_in, post_exists, user_owns_post


class NewPostHandler(CommonHandler):
    @post_exists
    @user_owns_post
    def update_post(self, title, body, *args, **kwargs):
        post = kwargs.get('post')
        post.title = title
        post.body = body
        post.put()

    def save_post(self, title, body):
        post = Post.save(title=title, body=body, author=self.user)
        post.put()
        self.redirect('/blog/' + str(post.key().id()))

    @user_logged_in
    def get(self):
        self.render("write.html")

    @user_logged_in
    def post(self):
        title = self.request.get('postTitle').strip()
        body = self.request.get('postBody').strip()
        post_id = self.request.get('postId')

        if not title or not body:
            self.render('write.html', post_title=title, post_body=body, error=True)
        else:
            # if post_id exist it means post is already created and we should update entity
            if post_id:
                self.update_post(self, title, body, post_id=post_id)
                self.redirect('/blog/' + str(post_id))
            else:
                self.save_post(title, body)
