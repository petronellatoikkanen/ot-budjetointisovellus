import unittest
from repositories.user_repository import user_repository
from repositories.budgeting_repository import budgeting_repository

from entities.user import User
from entities.budget import Budget
from entities.expense import Expense


class TestBudgetingRepository(unittest.TestCase):
    def setUp(self):
        budgeting_repository.delete_all()
        user_repository.delete_all()

        self.user = User('testi', 'testi123')
        self.budget = Budget('test_budget', 'testi')

    def test_create(self):
        budget = budgeting_repository.create(self.budget)

        self.assertEqual(budget.budget, self.budget.budget)