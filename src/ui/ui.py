from tkinter import Tk, ttk
from ui.create_user_view import CreateUserView
from ui.start_view import StartView
from ui.create_user_view import CreateUserView
from ui.budgeting_view import BudgetingView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_start_view()

    def create_user_view(self):
        self._current_view = CreateUserView(
            self._root,
            self.show_budgeting_view,
            self.show_start_view
        )

        self._current_view.pack()

    def hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def show_start_view(self):
        self.hide_current_view()

        self._current_view = StartView(
            self._root,
            self.show_budgeting_view,
            self.show_create_user_view
        )

        self._current_view.pack()

    def show_budgeting_view(self):
        self.hide_current_view()

        self._current_view = BudgetingView(
            self._root,
            self.show_start_view,
            self.show_budgeting_view,

        )

        self._current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self.show_budgeting_view,
            self.show_start_view
        )

        self._current_view.pack()
