import time

from blog_handler.Blog import BlogHandler
from blog_handler import Blog
from google.appengine.ext import db

from datatypes.Tag import Tag


class TagHandler(BlogHandler):
    def get(self):
        tags = db.GqlQuery("select * from Tag order by title desc")
        self.render("tags_page.html", tags = tags)
        
    def post(self):
        title = self.request.get('title')
        description = self.request.get('description')

        if title and description:
            p = Tag(parent = Blog.blog_key(), title = title, description = description)
            p.put()
            time.sleep(1)
            self.redirect('/blog/tags')
        else:
            error = "Title and Description, please!"
            self.render("tags_page.html", title=title, description=description, error=error)