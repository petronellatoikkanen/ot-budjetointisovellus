from entities.budget import Budget
from entities.expense import Expense
from repositories.budgeting_repository import (budgeting_repository as default_budgeting_repository)


class BudgetingService:
    def __init__(self, budgeting_repository=default_budgeting_repository):
        self.budget = None
        self.budgeting_repository = budgeting_repository

    def get_current_budget(self):
        return self.budget

    def get_budgets(self, user):
        return self.budgeting_repository.find_all(user)

    def create_budget(self, budget, username):
        self.budget = self.budgeting_repository.create(Budget(budget, username))
        return self.budget

    def add_new_expense(self, budget, expense, cost):
        return self.budgeting_repository.add_new_expense(Expense(expense, budget, cost))

    def get_expenses(self, budget):
        return self.budgeting_repository.find_budget_expenses(budget)

budgeting_service = BudgetingService()
