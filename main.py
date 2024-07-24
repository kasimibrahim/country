from tkinter import *
from countries import Countries
from PIL import Image, ImageTk
from controls import Controls
import random as r

window = Tk()
window.title("ROBOTICS GAME")
window.minsize(500, 500)

Label(window, text='WELCOME TO KNOW YOUR COUNTRIES').pack()

file = Image.open('./titleicon.png')
img = ImageTk.PhotoImage(file)
img_frame = Label(window, image=img)
img_frame.image = img
img_frame.pack()
score = 0

game = Countries(window)

bucketList = game.africa
if score > 50 and score <= 100:
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
    global img
    selected = r.choice(list(bucketList.keys()))
    current_question = bucketList[selected]
    img = PhotoImage(current_question.location)
    img_frame.config(image=img)
    img_frame.pack()
    current_question.show()
    print(current_question.location)


next = Button(window, text="NEXT", command=shuffle)
next.pack()
exit = Button(window, text='EXIT', command=exit)
exit.pack(side=BOTTOM)

window.mainloop()
