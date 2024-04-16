from tkinter import ttk, constants
from repositories import user_repository


class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self._root = root
        self.handle_login = handle_create_user
        self.handle_create_user_view = handle_show_login_view

        self.frame = None
        self.username_entry = None
        self.password_entry = None

        self.start()

    def start(self):

        self.frame = ttk.Frame(master=self._root)

        username_label = ttk.Label(master=self.frame, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=5, pady=5, sticky=constants.W)

        password_label = ttk.Label(master=self.frame, text="Password")
        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=5, pady=5, sticky=constants.W)

        self.frame.grid_columnconfigure(0, weight=1, minsize=1900)

        button = ttk.Button(master=self.frame, text="Create user",
                            command=self.create_user_handler)

        button.grid(padx=5, pady=5, sticky=constants.EW)

    def create_user_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Enter valid username and password")
            return

        try:
            user_repository.create_user(username, password)
            self.handle_create_user()
        except:
            print("Username already exists")

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
