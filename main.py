from tkinter import *
from countries import Countries
from controls import Controls
import random as r


"""
Name: Kasim Ibrahim
Robotics Game platform project 
"""
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
garbage = []
cleaner_size = 0
bucketList = game.africa
question_tracker = Countries(window).CountryQuestion('', window)


def shuffle():
    global question_tracker
    selected = r.choice(list(bucketList.keys()))
    while bucketList[selected] in garbage:
        selected = r.choice(list(bucketList.keys()))
    current_question = bucketList[selected]
    garbage.append(current_question)
    img = PhotoImage(file=current_question.location)
    img_frame.config(image=img)
    current_question.show()
    question_tracker = current_question
    print(current_question.location)
    while True:
        img_frame.update()


def submit():
    global score
    global bucketList
    global cleaner_size
    val = question_tracker.get_answer()
    print('answered:', val)
    try:
        print(game.shorthand[question_tracker.key])
        if val.lower() == game.shorthand[question_tracker.key].lower() and not question_tracker.attempt():
            score += 2
            print(score)
    except KeyError:
        print("CLICK ON NEXT FOR THE FIRST TIME")
        cleaner_size -= 1
    question_tracker.disable()
    cleaner_size += 1
    display_score.config(text='CURRENT SCORE: ' + str(score))
    display_score.update()

    if score > 50 and score <= 100:
        bucketList = game.asia
    elif score > 100 and score <= 120:
        bucketList = game.north_america
    elif score > 120 and score <= 130:
        bucketList = game.europe
    elif score > 130 and score <= 150:
        bucketList = game.south_america

    if cleaner_size == 6:
        for g in range(len(garbage)-1, -1, -1):
            garbage[g].get_entry().destroy()
            cleaner_size -= 1


nxt = Button(window, text="NEXT", command=shuffle)
submit = Button(window, text='SUBMIT', command=submit)

nxt.pack()
submit.pack()

ext = Button(window, text='EXIT', command=exit)
ext.pack(side=BOTTOM)

display_score = Label(window, text='CURRENT SCORE: ' + str(score))
display_score.pack(side=BOTTOM)

# if right:
#     score += 50
#     display_score.update()
#     print(score)
window.mainloop()
