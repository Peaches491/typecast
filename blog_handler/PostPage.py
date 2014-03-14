from blog_handler.Blog import BlogHandler
from blog_handler import Blog
from google.appengine.ext import db

from datatypes.Post import Post


class PostHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Blog.blog_key())
        post = db.get(key)
        
        if not post:
            self.error(404)
            self.render("404.html")
            return
        
        self.render("permalink.html", post = post)
        
        
class PostHandler_new(BlogHandler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
#             p = Post(parent = blog_key(), subject = subject, content = markdown2.markdown(content, extras=["fenced-code-blocks"]))
            p = Post(parent = Blog.blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)
            
