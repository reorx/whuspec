# -*- coding: utf-8 -*-


from torext.handlers import BaseHandler


class SigninHandler(BaseHandler):
    def get(self):
        self.render('user/signin.html')


class SignupHandler(BaseHandler):
    def get(self):
        self.render('user/signup.html')

    def post(self):
        pass


class InitHandler(BaseHandler):
    def get(self):
        self.render('user/init.html')


class DoneHandler(BaseHandler):
    def get(self):
        self.render('user/done.html')


handlers = [
    ('/signin', SigninHandler),
    ('/signup', SignupHandler),
    ('/init', InitHandler),
    ('/done', DoneHandler),
]
