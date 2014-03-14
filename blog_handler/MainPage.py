from blog_handler.Blog import BlogHandler

class MainPage(BlogHandler):
    def get(self):
        self.write('Hello, Udacity!')