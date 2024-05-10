from entities.user import User
from entities.budget import Budget
from database_connection import get_database_connection
from repositories import user_repository

def get_budget_by_row(row):
    return Budget(row["budget"], row["user"]) if row else None


class BudgetingRepository:
    def __init__(self, connection):
        self.user = None
        self.connection = connection

    def find_all(self):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from budgets"
        )

        row = cursor.fetchall()
        print(row)

       # return list(get_budget_by_row(row))

    def find(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from budgets where budget = ?",
            (budget,)
        )

        row = cursor.fetchall()

    def find_by_name(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from budgets where user = ?",
            (budget)
        )

        row = cursor.fetchall()


    def create(self, budget):
        cursor = self.connection.cursor()

        cursor.execute(
            "insert into budgets (budget, user) values (?, ?)",
            (budget.budget, budget.user)
        )
        
        self.connection.commit()

    def add_new_expense(self, budget, expense, sum):
        cursor = self.connection.cursor()

        cursor.execute(
            "insert into expenses (budget, expense, sum) values (), ?, ?)",
            (budget, expense, sum)
        )

        self.connection.commit()

    def delete_budget(self, budget):
        cursor = self.connection.cursor()

        cursor.execute("delete (budget) from budgets")

        cursor.execute("deop table (budget)")


        self.connection.commit()


budgeting_repository = BudgetingRepository(get_database_connection())