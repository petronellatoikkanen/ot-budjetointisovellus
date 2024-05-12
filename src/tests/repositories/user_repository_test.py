import unittest
from services.user_service import user_service
from repositories.user_repository import user_repository
from repositories.budgeting_repository import budgeting_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        budgeting_repository.delete_all()

        self.user = User('testi', 'testi123')

        self.username = 'testi'
        self.password = 'testi123'