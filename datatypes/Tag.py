from google.appengine.ext import db
from blog_handler import Blog


class Tag(db.Model):
    title = db.StringProperty(required = True)
    description = db.TextProperty(required = True)
    
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self, long=False):
        if long:
            return Blog.render_str("tag-long.html", t = self)
        else:
            return Blog.render_str("tag.html", t = self)