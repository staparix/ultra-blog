from google.appengine.ext import db
from model.User import Users


def post_key(group='default'):
    return db.Key.from_path('post', group)


class Post(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now_add=True)
    author = db.ReferenceProperty(Users, collection_name='author')

    @classmethod
    def save(cls, title, body, author):
        return Post(parent=post_key(), title=title, body=body, author=author)

    @classmethod
    def find_by_id(cls, post_id):
        key = db.Key.from_path('Post', post_id, parent=post_key())
        return db.get(key)

    @classmethod
    def by_id(cls, pid):
        return Post.get_by_id(pid, parent=post_key())
