from utilitites import markdown2
from google.appengine.ext import db

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self, key=None):
#         self._render_text = self.content.replace('\n', '<br>')
        self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
        if key:
            return render_str("post.html", p = self, permalink=key)
        else:
            return render_str("post.html", p = self)