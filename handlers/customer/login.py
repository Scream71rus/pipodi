
from handlers.base_handler import BaseHandler


class Login(BaseHandler):
    async def get(self):
        self.write('qweqwe')

    async def post(self):
        pass
