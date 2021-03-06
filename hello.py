#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File name    : hellp.py
Author       : miaoyc
Create date  : 2021/12/9 11:15 上午
Description  : tornado demo 
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.write("Hello, miaoyc!")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
                    (r"/", MainHandler),
                    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

