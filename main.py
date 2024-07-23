from tkinter import *
from countries import Countries
from controls import Controls
import random as r

window = Tk()
window.title("ROBOTICS GAME")
window.minsize(500, 500)

Label(window, text='WELCOME TO KNOW YOUR COUNTRIES').pack()

img = PhotoImage(file='titleicon.png')
img_frame = Label(window, image=img)
img_frame.pack()
score = 0

game = Countries(window)

if score <= 50:
    bucketList = game.africa
elif score > 50 and score <= 100:
    bucketList = game.asia
elif score > 100 and score <= 120:
    bucketList = game.north_america
elif score > 120 and score <= 130:
    bucketList = game.europe
elif score > 130 and score <= 150:
    bucketList = game.south_america
else:
    print("CONGRATULATIONS!")


# button = Controls(window, Button)
# start = button.answer_button('START GAME')
# start.pack()
# start.destroy()
# end = button.activate_exit_buttons('EXIT GAME')


def shuffle():
    selected = r.choice(list(bucketList.keys()))
    current_question = bucketList[selected]
    current_question.show()
    img_frame.config(image=PhotoImage(current_question.location))


nxt = Button(window, text="NEXT", command=shuffle)
nxt.pack()
ext = Button(window, text='EXIT', command=window.quit)
ext.pack()

window.mainloop()
