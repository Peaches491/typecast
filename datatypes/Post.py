from utilitites import markdown2
from google.appengine.ext import db
from blog_handler import Blog

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self, key=None):
#         self._render_text = self.content.replace('\n', '<br>')
        self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
        
        tags = db.GqlQuery("select * from Tag order by title desc")
        
        if key and tags:
            return Blog.render_str("post.html", p = self, permalink=key, tags=tags)
        else:
            return Blog.render_str("post.html", p = self)
