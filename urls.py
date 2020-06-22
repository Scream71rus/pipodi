
import tornado.web

from tornado.options import options
from handlers.customer.login import Login
from handlers.customer.registration import Registration

urls = [
    (r'/registration', Registration),
    (r'/login', Login),
    (r"/files/(.*)/?", tornado.web.StaticFileHandler, {"path": options.filestore}),
]
