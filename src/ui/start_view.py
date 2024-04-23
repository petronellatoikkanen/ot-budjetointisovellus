from tkinter import ttk, constants
from repositories import user_repository
from services import login_service


class StartView:
    def __init__(self, root, handle_login, handle_create_user_view):
        self._root = root
        self.handle_login = handle_login
        self.handle_create_user_view = handle_create_user_view

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

        button1 = ttk.Button(master=self.frame, text="Login",
                             command=self.login_handler)

        button2 = ttk.Button(
            master=self.frame, text="Not a user yet? Register here", command=self.handle_create_user_view)

        button1.grid(padx=5, pady=5, sticky=constants.EW)
        button2.grid(padx=5, pady=5, sticky=constants.EW)

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            login_service.login(username, password)
            self.handle_login()
        except:
            print("Wrong username or password")

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
