import unittest
from entities.user import User
from entities.budget import Budget

from services.user_service import (
    UserService,
    InvalidCredentialsError,
    UsernameExistsError)

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_user(self, username):
        users = filter(
            lambda user: user.username == username,
            self.users
        )
        users_list = list(users)

        return users_list[0] if len(users_list) > 0 else None

    def create(self, user):
        self.users.append(user)
        return user

    def delete_all(self):
        self.users = []

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())
        
        self.user = User('testi', 'testitesti')
        self.user2 = User('testaus', 'testaustestaus')
        
    def test_login_with_valid_credentials(self):
        self.user_service.create_user(self.user2.username, self.user2.password)
        user = self.user_service.login(self.user2.username,  self.user2.password)
        self.assertEqual(user.username, self.user2.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.user_service.login('t', 't')
        )

    def test_logout(self):
        user = self.user_service.logout()

        self.assertEqual(user, None)

    def test_create_user_with_unique_username(self):
        username = "unique"
        password = "uniquepass"

        user = self.user_service.create_user(username, password)

        self.assertEqual(user.username, username)

    def test_create_user_with_existing_username(self):
        self.user_service.create_user(self.user.username, 'testi123')

        self.assertRaises(
            UsernameExistsError,
            lambda: self.user_service.create_user(self.user.username, 'nottherightpass')
        )