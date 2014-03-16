import webapp2

from blog_handler.MainPage import MainPage
from blog_handler.BlogFront import BlogFront
from blog_handler.PostPage import PostHandler, PostHandler_new 
from blog_handler.StaticPage import StaticHandler, StaticHandler_new
from blog_handler.TagHandler import TagHandler


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/tags', TagHandler),
                               ('/blog/([0-9]+)', PostHandler),
                               ('/blog/newpost', PostHandler_new),
                               ('/blog/newpost/static', StaticHandler_new),
                               ('/blog/([a-zA-Z0-9]+)', StaticHandler),
                               ],
                               debug=True)
