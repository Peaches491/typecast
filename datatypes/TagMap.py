from google.appengine.ext import db

from datatypes.Post import Post
from datatypes.Tag import Tag 

class TagMap(db.Model):
    
    post_id = db.ReferenceProperty(Post, collection_name="post_id")
    tag_id  = db.ReferenceProperty(Tag, collection_name="tag_id")
    
    def render(self):
        pass
#         self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
#         return Blog.render_str("static.html", static = self)