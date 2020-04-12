
import json

import asyncpg
import aioredis
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import options
from tornado.ioloop import IOLoop

from models.base_model import BaseModel


class Application(tornado.web.Application):

    @property
    def httpclient(self):
        return self._httpclient

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._httpclient = tornado.httpclient.AsyncHTTPClient()

        IOLoop.current().spawn_callback(self.connect_to_db)
        IOLoop.current().spawn_callback(self.connect_to_cache)

    async def connect_to_db(self):
        BaseModel.db = await asyncpg.connect(database=options.db_name,
                                             user=options.db_user,
                                             password=options.db_password,
                                             host=options.db_host)

        await BaseModel.db.set_type_codec('json', encoder=json.dumps, decoder=json.loads, schema='pg_catalog')

    async def connect_to_cache(self):
        self.cache = await aioredis.create_redis_pool('redis://{}:{}'.format(options.cache_host, options.cache_port))
