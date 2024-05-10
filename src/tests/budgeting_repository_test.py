import unittest
from services.login_service import LoginService
from services.user_service import UserService
from services.budgeting_service import BudgetingService
from repositories.user_repository import UserRepository
from repositories.budgeting_repository import BudgetingRepository

from entities.user import User
from entities.budget import Budget


class TestBudgetingService(unittest.TestCase):
    def setUp(self):
        self.user = User('testi', 'testi123')
        self.username = 'testi'
        self.password = 'testi123'