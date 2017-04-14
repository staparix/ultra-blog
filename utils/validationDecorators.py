from model.Post import Post
from model.Comment import Comment


def user_logged_in(request_handler):
    def wrapper_handler(self, *args, **kwargs):
        if self.user:
            return request_handler(self, *args, **kwargs)
        else:
            self.redirect('/login')
            return

    return wrapper_handler


def post_exists(request_handler):
    def wrapper_handler(self, *args, **kwargs):
        post_id = kwargs.get('post_id')

        post = Post.find_by_id(int(post_id))
        if post:
            return request_handler(self, post=post, *args, **kwargs)
        else:
            self.error(404)
            return

    return wrapper_handler


def user_owns_post(request_handler):
    def wrapper_handler(self, *args, **kwargs):
        post = kwargs.get('post')
        if post.author.key().id() == self.user.key().id():
            return request_handler(*args, **kwargs)
        else:
            self.redirect('/')
            return

    return wrapper_handler


def comment_exists(request_handler):
    def wrapper_handler(self, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comment.find_by_id(int(comment_id))
        if comment:
            return request_handler(comment=comment, *args, **kwargs)
        else:
            self.redirect('/')
            return

    return wrapper_handler


def user_owns_comment(request_handler):
    def wrapper(self, *args, **kwargs):
        comment = kwargs.get('comment')
        if comment.comment_author.key().id() == self.user.key().id():
            return request_handler(self, *args, **kwargs)
        else:
            self.redirect('/')
            return

    return wrapper
