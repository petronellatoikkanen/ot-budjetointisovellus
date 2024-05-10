from tkinter import ttk, constants
from repositories.user_repository import user_repository
from services.login_service import login_service


class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        self.root = root
        self.handle_login = handle_login
        self.handle_show_create_user_view = handle_show_create_user_view

        self.frame = None
        self.username_entry = None
        self.password_entry = None

        self.start()

    def start(self):

        self.frame = ttk.Frame(master=self.root)

        username_label = ttk.Label(master=self.frame, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.username_entry.grid(padx=5, pady=5, sticky=constants.W)

        password_label = ttk.Label(master=self.frame, text="Password")
        self.password_entry = ttk.Entry(master=self.frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.password_entry.grid(padx=5, pady=5, sticky=constants.W)

        login_button = ttk.Button(master=self.frame, text="Login",
                             command=self.login_handler)

        create_user_button = ttk.Button(master=self.frame, text="Not a user yet? Register here", 
                             command=self.handle_show_create_user_view)

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.frame.grid_columnconfigure(1, weight=0)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
    

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login_service.login(username, password):
            self.handle_login()
        else:
            pass

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
