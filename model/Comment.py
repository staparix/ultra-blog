from google.appengine.ext import db
from model.Post import Post
from model.User import Users


def comment_key(group='default'):
    return db.Key.from_path('comment', group)


class Comment(db.Model):
    comment_author = db.ReferenceProperty(Users, collection_name='comment_author', required=True)
    post = db.ReferenceProperty(Post, collection_name='blog_post', required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def save(cls, author, post, comment):
        return Comment(parent=comment_key(),
                       comment_author=author,
                       post=post,
                       comment=comment)

    @classmethod
    def by_id(cls, pid):
        return Comment.get_by_id(pid, parent=comment_key())
