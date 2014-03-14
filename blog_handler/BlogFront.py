from blog_handler.Blog import BlogHandler
from google.appengine.ext import db

class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery("select * from Post order by created desc limit 10")
        keys = db.GqlQuery("select __key__ from Post order by created desc limit 10")
        keys = ["/blog/" + str(key.id()) for key in keys]
        self.render('front.html', posts = zip(keys, posts))

