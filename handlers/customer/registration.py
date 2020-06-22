
import os
import hashlib

from handlers.base_handler import BaseHandler
from models.customer_model import CustomerModel


class Registration(BaseHandler):

    async def get(self):
        self.render('registration.html', message=None)

    async def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        password_2 = self.get_argument('password_2')

        if password and password_2 and password == password_2:
            password = hashlib.sha256(password.encode()).hexdigest()

        customer = await CustomerModel.get_by_email(email=email)
        if customer is None:
            customer = await CustomerModel.create(email=email, password=password)
            session_key = os.urandom(8).hex()

            await self.set_cache('pipodi_session_key_{}'.format(session_key), customer)
            self.set_cookie('pipodi_session_key', session_key)

            self.redirect('/')

        else:
            self.render('registration.html', message='Пользователь с таким Email уже существует')
