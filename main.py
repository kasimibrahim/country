from tkinter import *
from countries import Countries
from controls import Controls
import random as r

window = Tk()
window.title("ROBOTICS GAME")
window.minsize(500, 500)

Label(window, text='WELCOME TO KNOW YOUR COUNTRIES').pack()

file = PhotoImage(file='./titleicon.png')
img_frame = Label(window, image=file)
img_frame.pack()
score = 0

game = Countries(window)
right = False

bucketList = game.africa
question_tracker = Countries(window).CountryQuestion('', window)

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


def shuffle():
    global question_tracker
    selected = r.choice(list(bucketList.keys()))
    current_question = bucketList[selected]
    img = PhotoImage(file=current_question.location)
    img_frame.config(image=img)
    current_question.show()
    question_tracker = current_question
    print(current_question.location)
    while True:
        img_frame.update()


def submit():
    global right
    val = question_tracker.get_answer()
    print('answered:', val)
    print(game.shorthand[question_tracker.key])
    right = val == game.shorthand[question_tracker.key]


nxt = Button(window, text="NEXT", command=shuffle)
submit = Button(window, text='SUBMIT', command=submit)
nxt.pack()
submit.pack()

ext = Button(window, text='EXIT', command=exit)
ext.pack(side=BOTTOM)

display_score = Label(window, text='CURRENT SCORE: '+str(score))
display_score.pack(side=BOTTOM)

if right:
    score += 50
    display_score.update()
    print(score)
window.mainloop()
