import countries
from tkinter import *
class Controls:
    def __init__(self, tk, button):
        self.tk = tk
        self.button = button

    def activate_exit_buttons(self, info):
        return self.button(self.tk, text=info, command=self.tk.quit)

    def answer_button(self, info):
        return self.button(self.tk, text=info, command=countries.Countries(self.tk).shuffle)


