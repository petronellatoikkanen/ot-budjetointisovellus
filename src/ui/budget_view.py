from tkinter import ttk, constants
from services.budgeting_service import budgeting_service

class BudgetView:
    def __init__(self, root, budgets, handle_add_expense):
        self.root = root
        self.budgets = budgets
        self.handle_add_expense = handle_add_expense
        self.frame = None

        self.start()

    def start(self):
        self.frame = ttk.Frame(master=self.root)

        item_frame = ttk.Frame(master=self.frame)

        label = ttk.Label(master=item_frame, text=budget.budget)

        expense_label = ttk.Label(master=self.frame, text="Expense")
        self.expense_entry = ttk.Entry(master=self.frame)

        expense_label.grid(padx=5, pady=5, sticky=constants.W)
        self.expense_entry.grid(padx=5, pady=5, sticky=constants.W)

        sum_label = ttk.Label(master=self.frame, text="Sum")
        self.sum_entry = ttk.Entry(master=self.frame)

        sum_label.grid(padx=5, pady=5, sticky=constants.W)
        self.sum_entry.grid(padx=5, pady=5, sticky=constants.W)

        add_new_expense_button = ttk.Button(
            master=item_frame,
            text="Add new expense",
            command=lambda: self.handle_add_expense(budget)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        add_new_expense_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def handle_add_new_expense(self, budget):
        expense = self.expense_entry.get()
        sum = self.sum_entry.get()

        if expense and sum:
            budgeting_service.add_new_expense(budget, expense, sum)
            expense = self.add_new_expense.delete()
            sum = self.enter_sum.delete()

        self.budget_list()