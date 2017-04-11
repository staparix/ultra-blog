from google.appengine.ext import db

from model.User import Users
from model.Post import Post


class Like(db.Model):
    user = db.ReferenceProperty(Users, collection_name='user')
    post = db.ReferenceProperty(Post, collection_name='post')
