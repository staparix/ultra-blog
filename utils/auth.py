import random
import hashlib
from string import letters


def valid_pw(username, pw, h):
    return h == make_pw_hash(username, pw, h.split(',')[1])


def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()

    return '%s,%s' % (h, salt)
