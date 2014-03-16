from utilitites import markdown2
from google.appengine.ext import db
from blog_handler import Blog

from datatypes.Tag import Tag 
from datatypes.Post import Post

class TagMap(db.Model):
    
    post_id = db.ReferenceProperty(reference_class=Post)
    tag_id  = db.ReferenceProperty(reference_class=Tag)
    
    def render(self, key=None):
#         self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
#         return Blog.render_str("static.html", static = self)