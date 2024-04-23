from tkinter import ttk, constants


class BudgetingView:
    def __init__(self, root, budgeting, handle_budget):
        self._root = root
        self.handle_login = budgeting
        self.handle_create_user_view = handle_budget

        self.frame = None

        self.start()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()