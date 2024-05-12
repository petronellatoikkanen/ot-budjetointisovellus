from tkinter import ttk, constants
from services.user_service import user_service
from services.budgeting_service import budgeting_service
from repositories.budgeting_repository import budgeting_repository


class BudgetListView:
    def __init__(self, root, budgets):
        self.root = root
        self.budgets = budgets

        self.frame = None

        self.add_for_budget_entry = None
        self.add_expense_entry = None
        self.add_cost_entry = None

        self.start()

    def start(self):
        self.frame = ttk.Frame(master=self.root)

        for budget in self.budgets:      
            item_frame = ttk.Frame(master=self.root)
            label = ttk.Label(master=item_frame, text=budget.budget)
            label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        self.expenses = budgeting_service.get_expenses(budget.budget)
        if self.expenses:
            for expense in self.expenses:
                exp_frame = ttk.Frame(master=self.root)

                exp_label = ttk.Label(master=exp_frame, text=expense.expense)
                exp_label.grid(padx=5, pady=5, sticky=constants.W)

                cost_label = ttk.Label(master=exp_frame, text=expense.cost)
                cost_label.grid(padx=5, pady=5, sticky=constants.W)

                exp_frame.grid_columnconfigure(2, weight=1)
                exp_frame.pack(fill=constants.X)

        item_frame.grid_columnconfigure(1, weight=1)
        item_frame.pack(fill=constants.X)


        add_expense_button = ttk.Button(
            master=self.frame,
            text="Add Expense",
            command=self.handle_add_expense
        )
        
        add_for_budget_label = ttk.Label(master=self.frame, text="Budget")
        self.add_for_budget_entry = ttk.Entry(master=self.frame)
    
        add_for_budget_label.grid(padx=5, pady=5, sticky=constants.W)
        self.add_for_budget_entry.grid(padx=5, pady=5, sticky=constants.W)
          
        add_expense_label = ttk.Label(master=self.frame, text="New expense")
        self.add_expense_entry = ttk.Entry(master=self.frame)
    
        add_expense_label.grid(padx=5, pady=5, sticky=constants.W)
        self.add_expense_entry.grid(padx=5, pady=5, sticky=constants.W)
    
        add_cost_label = ttk.Label(master=self.frame, text="cost")
        self.add_cost_entry = ttk.Entry(master=self.frame)
        
        add_cost_label.grid(padx=5, pady=5, sticky=constants.W)
        self.add_cost_entry.grid(padx=5, pady=5, sticky=constants.W)

        add_expense_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )


    def handle_add_expense(self):
        expense = self.add_expense_entry.get()
        budget = self.add_for_budget_entry.get()
        cost = self.add_cost_entry.get()

        if expense and budget and cost:
            budgeting_service.add_new_expense(expense, budget, cost)
            self.add_expense_entry.delete(0, constants.END)
            self.add_for_budget_entry.delete(0, constants.END)
            self.add_cost_entry.delete(0, constants.END)

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
            row=4,
            column=0,
            columnspan=3,
            sticky=constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=500)
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

        budgets = budgeting_service.get_budgets(self.user.username)

        if budgets:
            self.budget_list_view = BudgetListView(
                self.budget_list_frame,
                budgets,
            )

            self.budget_list_view.pack()

        else:
            self.handle_create_budget



    def handle_create_budget(self):
        budget = self.create_new_budget.get()

        if budget:
            budgeting_service.create_budget(budget, self.user.username)
            self.budget_list
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
        user_service.logout()
        self.handle_logout()


    def pack(self):
        self.frame.pack(fill=constants.X)


    def destroy(self):
        self.frame.destroy()