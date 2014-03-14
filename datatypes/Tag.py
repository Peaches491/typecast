from utilitites import markdown2
from google.appengine.ext import db
from blog_handler import Blog


class StaticPage(db.Model):
    title = db.StringProperty(required = True)
    description = db.TextProperty(required = True)
    
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self, key=None):
#         self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
#         return Blog.render_str("static.html", static = self)