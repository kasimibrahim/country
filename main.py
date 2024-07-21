from tkinter import *
from tkinter import messagebox

from controls import Controls

window = Tk()
window.title("ROBOTICS GAME")
window.minsize(500, 500)


Label(window, text='WELCOME TO KNOW YOUR COUNTRIES').pack()


img = PhotoImage(file='./countries/ghana.png')
img_frame = Label(window, image=img)
img_frame.pack()




button = Controls(window, Button)
start = button.answer_button('START GAME')
start.pack()
start.destroy()
end = button.activate_exit_buttons('EXIT GAME')


if not end.pack():
    button.answer_button('NEXT').pack()





window.mainloop()
