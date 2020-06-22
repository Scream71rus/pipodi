
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

    async def set_cache(self, key, value, ex=None):
        value = pickle.dumps(value)
        if ex:
            await self.cache.set(key, value, ex=ex)
        else:
            await self.cache.set(key, value)

    async def prepare(self):
        session_key = self.get_cookie('pipodi_session_key')
        if session_key:
            self.customer = await self.get_cache('pipodi_session_key_{}'.format(session_key))
