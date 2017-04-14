from handlers.common.CommonHandler import CommonHandler
from utils.validationDecorators import post_exists, user_owns_post, user_logged_in


class EditPostHandler(CommonHandler):
    @post_exists
    @user_owns_post
    def edit_post(self, *args, **kwargs):
        post = kwargs.get('post')
        post_id = kwargs.get('post_id')
        self.render('write.html', post_id=post_id, post_title=post.title, post_body=post.body, edit=True)

    @user_logged_in
    def get(self, post_id):
        self.edit_post(self, post_id=post_id)
