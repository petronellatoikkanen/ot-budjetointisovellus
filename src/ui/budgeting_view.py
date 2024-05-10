from tkinter import ttk, constants
from services.user_service import user_service
from services.login_service import login_service
from services.budgeting_service import budgeting_service
from repositories.budgeting_repository import budgeting_repository
from ui.budget_view import BudgetView

class BudgetListView:
    def __init__(self, root, budgets, handle_open_budget):
        self.root = root
        self.budgets = budgets
        self.handle_open_budget = handle_open_budget
        self.frame = None

        self.start()

    def start(self):
        self.frame = ttk.Frame(master=self.root)

        for budget in self.budgets:
            item_frame = ttk.Frame(master=self.frame)

            label = ttk.Label(master=item_frame, text=budget.budget)

            add_new_expense_button = ttk.Button(
                master=item_frame,
                text="Open budget",
                command=lambda: self.handle_open_budget(budget)
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


class BudgetingView:
    def __init__(self, root, handle_logout):
        self.root = root
        self.handle_logout = handle_logout
        self.user = user_service.get_current_user()

        self.create_budget = None

        self.budget_list_frame = None
        self.budget_list_view = None

        self.frame = None

        self.start()

    def start(self):
        self.frame = ttk.Frame(master=self.root)
        self.budget_list_frame = ttk.Frame(master=self.frame)

        self.header()
        self.budget_list()
        self.footer()

        self.budget_list_frame.grid(
            row=2,
            column=1,
            columnspan=3,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=1900)
        self.frame.grid_columnconfigure(1, weight=0)


    def header(self):
        user_label = ttk.Label(
            master=self.frame,
            text=f"Welcome {self.user.username}! Have a great day of budgeting!"
        )

        logout_button = ttk.Button(
            master=self.frame,
            text="Logout here",
            command=self.logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )


    def budget_list(self):
        if self.budget_list_view:
            self.budget_list_view.destroy()

        budgets = budgeting_service.get_budgets()
        print(budgets)

        if budgets:

            self.budget_list_view = BudgetListView(
                self.budget_list_frame,
                budgets,
                self.handle_open_budget
            )

            self.budget_list_view.pack()

        else:
            self.handle_create_budget


    def handle_add_new_expense(self, budget):
        expense = self.expense_entry.get()
        sum = self.sum_entry.get()

        if expense and sum:
            budgeting_service.add_new_expense(budget, expense, sum)
            expense = self.add_new_expense.delete()
            sum = self.enter_sum.delete()

        self.budget_list()


    def handle_create_budget(self):
        budget = self.create_new_budget.get()

        if budget:
            budgeting_service.create_budget(budget, self.user.username)
            self.create_new_budget.delete(0, constants.END)

        self.budget_list()
    

    def footer(self):
        self.create_new_budget = ttk.Entry(master=self.frame)

        create_new_budget_button = ttk.Button(
            master=self.frame,
            text="Create new budget",
            command=self.handle_create_budget
        )

        self.create_new_budget.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        create_new_budget_button.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
        )

    def logout_handler(self):
        login_service.logout()
        self.handle_logout()


    def pack(self):
        self.frame.pack(fill=constants.X)


    def destroy(self):
        self.frame.destroy()