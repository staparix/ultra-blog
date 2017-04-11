import webapp2

from handlers.BlogFrontHandler import BlogFrontHandler
from handlers.DeleteCommentHandler import DeleteCommentHandler
from handlers.DeletePostHandler import DeletePostHandler
from handlers.EditCommentHandler import EditCommentHandler
from handlers.EditPostHandler import EditPostHandler
from handlers.LogoutHandler import LogoutHandler
from handlers.NewCommentHandler import NewCommentHandler
from handlers.NewPostHandler import NewPostHandler
from handlers.PostDetailsHandler import PostDetailsHandler
from handlers.RegistrationHandler import RegistrationHandler
from handlers.MainHandler import Main
from handlers.LikeHandler import LikeHandler
from handlers.LoginHandler import LoginHandler

app = webapp2.WSGIApplication([
    ('/', Main),
    ('/blog/?', BlogFrontHandler),
    ('/blog/newpost', NewPostHandler),
    ('/blog/(\d+)', PostDetailsHandler),
    ('/edit/(\d+)', EditPostHandler),
    ('/signup', RegistrationHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/like', LikeHandler),
    ('/post/delete', DeletePostHandler),
    ('/comment', NewCommentHandler),
    ('/comment/delete', DeleteCommentHandler),
    ('/post/(\d+)/edit/comment/(\d+)', EditCommentHandler)

], debug=True)
