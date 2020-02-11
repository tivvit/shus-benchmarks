import sys
import tornado.ioloop
import tornado.web

from tornado.httpserver import HTTPServer

from utils import configure
from utils import configure_backend
from utils import configure_cache

conf = configure("conf.yml")
backend = configure_backend(conf)
if not backend:
    print("backend is not configured")
    sys.exit(1)
urls = configure_cache(conf, backend)


class MainHandler(tornado.web.RequestHandler):
    def get(self, short):
        if short not in urls:
            raise tornado.web.HTTPError(status_code=404)
        self.redirect(urls.get(short))


def make_app():
    return tornado.web.Application([
        (r"/([A-Za-z0-9]+)", MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    server = HTTPServer(app)
    server.bind(80)
    server.start(0)  # Forks multiple sub-processes
    tornado.ioloop.IOLoop.current().start()
