from entities.budget import Budget
from repositories.budgeting_repository import (budgeting_repository as default_budgeting_repository)



class BudgetingService:
    def __init__(self):
        self.budget = None
        self.budgeting_repository = default_budgeting_repository

    def get_current_budget(self):
        return self.budget

    def get_budgets(self):
        return self.budgeting_repository.find_all()
    
    def create_budget(self, budget, username):
        if self.budgeting_repository.find(budget):
            print("not ok, already exists")
            pass

        budget = Budget(budget, username)

        return self.budgeting_repository.create(budget)
    
    def add_new_expense(self, budget, expense, sum):
        if not self.budgeting_repository.find(budget):
            print("not ok, budget does not exists")
            pass

        return self.budgeting_repository.add_new_expense(budget)
    

budgeting_service = BudgetingService()