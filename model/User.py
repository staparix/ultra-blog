from google.appengine.ext import db
from utils import auth


def users_key(group='default'):
    return db.Key.from_path('users', group)


class Users(db.Model):
    username = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, uid):
        return Users.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, username):
        u = Users.all().filter('username =', username).get()
        return u

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and auth.valid_pw(name, pw, u.pw_hash):
            return u

    @classmethod
    def register(cls, username, pw, email=None):
        pw_hash = auth.make_pw_hash(username, pw)
        print pw_hash
        return Users(parent=users_key(),
                     username=username,
                     pw_hash=pw_hash,
                     email=email)
