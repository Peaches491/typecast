from blog_handler.Blog import BlogHandler
from blog_handler import Blog
from google.appengine.ext import db
import logging

from datatypes.Post import Post
from datatypes.TagMap import TagMap


class PostHandler(BlogHandler):
    
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=Blog.blog_key())
        post = db.get(key)
        
        if not post:
            self.error(404)
            self.render("404.html")
            return
        
        self.render("permalink.html", post = post)
        
    def post(self, post_id):
        
        key = db.Key.from_path('Post', int(post_id), parent=Blog.blog_key())
        post = db.get(key)
        
        post_key = self.request.get('post_key')
        tag_key = self.request.get('tag_key')
        
        query = "select * from TagMap WHERE post_id = key('{}') and tag_id = key('{}')".format(post_key, tag_key)
        tags = db.GqlQuery(query).count(1);
        
        if tags != 0:
            error = "This Tag has already been applied to this Post!"
            self.render("permalink.html", post = post, post_key=post_key, tag_key=tag_key, error=error)
        elif post_key and tag_key:
            p = TagMap( parent = Blog.blog_key(), post_id = db.get(post_key), tag_id = db.get(tag_key) )
            p.put()
            self.redirect('/blog/')
        else:
            error = "Post and Tag keys, please!"
            self.render("permalink.html", post_key=post_key, tag_key=tag_key, error=error)
           
        
        
class PostHandler_new(BlogHandler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = Blog.blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)
            
