
import tornado.web

from tornado.options import options
from handlers.customer.login import Login

urls = [
    (r'/login', Login),
    (r"/files/(.*)/?", tornado.web.StaticFileHandler, {"path": options.filestore}),
]
