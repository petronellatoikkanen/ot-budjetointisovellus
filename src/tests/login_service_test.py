import unittest
from services.login_service import LoginService
from services.user_service import UserService
from repositories.user_repository import UserRepository

from entities.user import User

class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.user = User('testi', 'testi123')
        self.username = 'testi'
        self.password = 'testi123'
       # self.create(self, self.user)
       # self.login_service = LoginService(UserRepository())


    def test_login(self):
        user = self.login(self.username, self.password)

        self.assertEqual(user, self.user)

    def test_logout(self):
        user = self.logout()

        self.assertEqual(user, None)
