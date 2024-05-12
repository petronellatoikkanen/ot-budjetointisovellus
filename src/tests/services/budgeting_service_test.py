import unittest
from entities.user import User
from entities.budget import Budget
from entities.expense import Expense
from services.budgeting_service import BudgetingService
from services.user_service import user_service

class FakeBudgetingRepository:
    def __init__(self, budgets=None, expenses=None):
        self.budgets = budgets or []
        self.expenses = expenses or []

    def find_all(self):
        return self.todos

    def find(self, username):
        user_budgets = filter(
            lambda budget: budget.user and budget.user.username == username,
            self.budgets
        )

        user_budgets_list = list(user_budgets)

        return user_budgets_list

    def create(self, budget):
        self.budgets.append(budget)

        return budget

    def add_new_expense(self, expense):
        self.expenses.append(expense)

        return expense
    
    def delete_all(self):
        self.budgets = []
        self.expenses = []
  

class TestBudgetingService(unittest.TestCase):
    def setUp(self):
        self.budgeting_service = BudgetingService(FakeBudgetingRepository())
        self.user = User('testi2', 'testi123')
        self.budget = Budget('testibudjetti', 'testi')
        self.expense = Expense('testiexpense', 'testibudjetti', '100')
    
    def login_user(self, user):
        user_service.create_user(user.username, user.password)

    def test_create_budget(self):
        self.login_user(self.user)

        budget = self.budgeting_service.create_budget(self.budget.budget, self.budget.user)

        self.assertEqual(budget.budget, self.budget.budget)

    def test_add_new_expense(self):
        expense = self.budgeting_service.add_new_expense(self.expense.expense, self.expense.budget, self.expense.cost)

        self.assertEqual(expense.expense, self.expense.expense)