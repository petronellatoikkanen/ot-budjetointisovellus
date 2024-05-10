from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.budgeting_view import BudgetingView
from ui.budget_view import BudgetView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_login_view()


    def hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def show_login_view(self):
        self.hide_current_view()

        self._current_view = LoginView(
            self._root,
            self.show_budgeting_view,
            self.show_create_user_view
        )

        self._current_view.pack()

    def show_budgeting_view(self):
        self.hide_current_view()

        self._current_view = BudgetingView(
            self._root,
            self.show_login_view,
        )

        self._current_view.pack()


    def show_create_user_view(self):
        self.hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self.show_budgeting_view,
            self.show_login_view
        )

        self._current_view.pack()
