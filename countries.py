from tkinter import *
import random as r
import controls


class Countries:
    def __init__(self, tk):
        self.tk = tk
        self.score = 0
        self.current_question = Label()
        self.africa = {
            1: Countries.CountryQuestion('ghana'.lower(), tk),
            2: Countries.CountryQuestion('Mali'.lower(), tk)

        }
        self.asia = {}
        self.europe = {}
        self.north_america = {}
        self.south_america = {}

    def shuffle(self):
        del self.current_question
        selected = r.choice(list(self.africa.keys()))
        self.current_question = self.africa[selected]

        self.current_question.show()

    class CountryQuestion:
        def __init__(self, key, tk):
            self.key = key
            self.location = './countries/'+key+'.png'
            self.entry = Entry(tk)

        def show(self):
            # self.label.grid(row=1, column=1)
            # self.entry.grid(row=1, column=2)
            self.entry.pack()


def check_answer(image_directory, question):
    return image_directory == question.location
