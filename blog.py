import os
from utilitites import markdown2

import webapp2, logging
import jinja2

from google.appengine.ext import db
from data import *



template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

class MainPage(BlogHandler):
    def get(self):
        self.write('Hello, Udacity!')

##### blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

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
        
class StaticPage(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    brief = db.TextProperty(required = True)
    url = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self, key=None):
        self._render_text = markdown2.markdown(self.content, extras=["fenced-code-blocks"])
        return render_str("static.html", static = self)

class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery("select * from Post order by created desc limit 10")
        keys = db.GqlQuery("select __key__ from Post order by created desc limit 10")
        keys = ["/blog/" + str(key.id()) for key in keys]
        self.render('front.html', posts = zip(keys, posts))

class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        
        if not post:
            self.error(404)
            self.render("404.html")
            return
        
        self.render("permalink.html", post = post)

class NewPost(BlogHandler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
#             p = Post(parent = blog_key(), subject = subject, content = markdown2.markdown(content, extras=["fenced-code-blocks"]))
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)
            
class NewPost_static(BlogHandler):
    def get(self):
        self.render("newpost_static.html")

    def post(self):
        title = self.request.get('title')
        brief = self.request.get('brief');
        url = self.request.get('url');
        content = self.request.get('content')
        
        if title and content:
            p = StaticPage(parent = blog_key(), title = title, brief = brief, url=url, content = content)
            p.put()
            self.redirect('/blog/%s' % url)
        else:
            error = "subject and content, please!"
            self.render("newpost.html", title=title, brief=brief, content=content, error=error)

class Static(BlogHandler):
    def get(self, page_title):
        
        pages = db.GqlQuery("select * from StaticPage where url = '%s'" % page_title)
        page = pages.get()
        
        if page:
            page.content = markdown2.markdown(page.content, extras=["fenced-code-blocks"])
            logging.debug("Page url is: %s" % page.url)
            self.render("permalink.html", post=page)
        else:
            self.error(404)
            self.render("404.html")


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/newpost/static', NewPost_static),
                               ('/blog/([a-zA-Z0-9]+)', Static),
                               ],
                               debug=True)

