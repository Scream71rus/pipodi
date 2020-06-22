
import hashlib
import os

from handlers.base_handler import BaseHandler
from models.customer_model import CustomerModel


class Login(BaseHandler):
    async def get(self):
        self.write('qweqwe')

    async def post(self):
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        password = hashlib.sha256(password.encode()).hexdigest() if password else None

        customer = await CustomerModel.get_by_email(email=email)
        if customer:
            session_key = os.urandom(8).hex()

            await self.set_cache('pipodi_session_key_{}'.format(session_key), customer)
            self.set_cookie('pipodi_session_key', session_key)

            self.redirect('/')

        else:
            self.redirect('/login')
