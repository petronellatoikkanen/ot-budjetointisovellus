from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Budgeting Application")
        
        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)


        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Login")
        
        label.grid(row=0, column=1)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        button.grid(row=3, column=1)