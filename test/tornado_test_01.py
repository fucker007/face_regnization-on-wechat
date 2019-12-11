import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.options

tornado.options.define("port", default=33333, help="run on the given port", type=int)


class XiaoduExtractor(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello!!!")

    def post(self):
        pass


def create_server():
    tornado.options.parse_command_line()
    web_app = tornado.web.Application(handlers=[(r"/", XiaoduExtractor)])
    http_server = tornado.httpserver.HTTPServer(web_app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    create_server()