
import pickle
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    @property
    def cache(self):
        return self.application.cache

    @property
    def httpclient(self):
        return self.application.httpclient

    async def get_cache(self, key):
        value = await self.cache.get(key, encoding='utf-8')
        try:
            return pickle.loads(value) if value else None
        except:
            return None

    def set_cache(self, key, value, ex=None):
        value = pickle.dumps(value)
        self.cache.set(key, value, ex=ex)

    def prepare(self):
        pass
