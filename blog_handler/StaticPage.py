from google.appengine.ext import db
import logging
from utilitites import markdown2

from blog_handler import Blog
from blog_handler.Blog import BlogHandler

from datatypes.Static import StaticPage 


class StaticHandler(BlogHandler):
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
            
            
class StaticHandler_new(BlogHandler):
    def get(self):
        self.render("newpost_static.html")

    def post(self):
        title = self.request.get('title')
        brief = self.request.get('brief');
        url = self.request.get('url');
        content = self.request.get('content')
        
        if title and content:
            p = StaticPage(parent = Blog.blog_key(), title = title, brief = brief, url=url, content = content)
            p.put()
            self.redirect('/blog/%s' % url)
        else:
            error = "subject and content, please!"
            self.render("newpost.html", title=title, brief=brief, content=content, error=error)