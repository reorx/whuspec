#!/usr/bin/env python
# -*- coding: utf-8 -*-


from torext.handlers import BaseHandler


class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html')


handlers = [
    ('/', HomeHandler),
]
