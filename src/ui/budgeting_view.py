from tkinter import ttk, constants


class BudgetingView:
    def __init__(self, root, budgeting, handle_budget):
        self._root = root
        self.handle_login = budgeting
        self.handle_create_user_view = handle_budget

        self.frame = None

        self.start()

    def start(self):

        self.frame = ttk.Frame(master=self._root)

        budgets_label = ttk.Label(master=self.frame, text="Budgets")
        # self.budgets_entry = ttk.Entry(master=self.frame)

        budgets_label.grid(padx=5, pady=5, sticky=constants.W)
        #self.budgets_entry.grid(padx=5, pady=5, sticky=constants.W)

        new_budgets_label = ttk.Label(master=self.frame, text="Create new budgets")
        self.new_budgets_entry = ttk.Entry(master=self.frame)

        new_budgets_label.grid(padx=5, pady=5, sticky=constants.W)
        self.new_budgets_entry.grid(padx=5, pady=5, sticky=constants.W)

        self.frame.grid_columnconfigure(0, weight=1, minsize=1900)

        button = ttk.Button(master=self.frame, text="Create budget",
                            command=self.handle_create_budget)

        button.grid(padx=5, pady=5, sticky=constants.EW)


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()