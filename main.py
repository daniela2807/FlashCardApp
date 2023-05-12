import random
import time

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
p = {}
french= ""
english = ""


canvas = Canvas(width=800, height=525, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=card_front)
canvas.config(background=BACKGROUND_COLOR)
english_text=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
french_text=canvas.create_text(400,283,text="Word",font=("Arial",60,"bold"))
canvas.grid(row=0, column=0,columnspan=2)


##ReadCSV
def read_csv():
    global p
    df = pd.read_csv('./data/french_words.csv',index_col=0,header=0)
    p=df.to_dict()
    p=p["English"]
    for key,value in p.items():
        print(key,':',value)

def show_new():
    global english,french,flip_timer
    window.after_cancel(flip_timer)
    french, english = random.choice(list(p.items()))
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(english_text, text="French")
    canvas.itemconfig(french_text, text=french)
    flip_timer=window.after(3000, func=change_words)


def change_words():
    global english
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(english_text, text="English")
    canvas.itemconfig(french_text, text=english)



flip_timer = window.after(3000,func=change_words)
read_csv()
show_new()

filename2 = PhotoImage(file="images/wrong.png")
rigth_button = Button(image=filename2,highlightthickness=0,command=show_new)
rigth_button.grid(row=1, column=0)

filename3 = PhotoImage(file="images/right.png")
left_button = Button(image=filename3,highlightthickness=0,command=show_new)
left_button.grid(row=1, column=1)


window.mainloop()