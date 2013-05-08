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


handlers = [
    ('/signin', SigninHandler),
    ('/signup', SignupHandler),
]
