# -*- coding: utf-8 -*-

from torext.handlers import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.render('spec/index.html')


handlers = [
    ('', IndexHandler),
]
