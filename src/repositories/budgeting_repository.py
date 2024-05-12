from entities.budget import Budget
from entities.expense import Expense
from database_connection import get_database_connection

def get_budget_by_row(row):
    return Budget(row[1], row[2]) if row else None

def get_expenses_by_row(row):
    return Expense(row[1], row[2], row[3]) if row else None

class BudgetingRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_all(self, username):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from budgets where user = ?",
            (username,)
        )

        rows = cursor.fetchall()

        return list(map(get_budget_by_row, rows))

    def find(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from budgets where budget = ?",
            (budget,)
        )

        row = cursor.fetchone()

        return get_budget_by_row(row)

    def find_budget_expenses(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from expenses where budget = ?",
            (budget,)
        )

        rows = cursor.fetchall()

        return list(map(get_expenses_by_row, rows))

    def create(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "insert into budgets (budget, user) values (?, ?)",
            (budget.budget, budget.user)
        )

        self.connection.commit()

        return budget

    def add_new_expense(self, expense):
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into expenses (expense, budget, cost) values (?, ?, ?)",
            (expense.expense, expense.budget, expense.cost)
        )

        self.connection.commit()

        return expense

    def delete_all(self):
        cursor = self.connection.cursor()

        cursor.execute("delete from budgets")

        self.connection.commit()

budgeting_repository = BudgetingRepository(get_database_connection())
