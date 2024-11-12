from tkinter import Tk, Button, Canvas, PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English", fill ="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background , image = card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back =PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front)
card_title = canvas.create_text(400, 150, text="Title" , font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word" , font=("Ariel", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column = 0, row = 0, columnspan =2)

flip_timer = window.after(3000, func=flip_card)

unknown_img = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
cancel_button.grid(column =0, row = 1)

check_img = PhotoImage(file="images/right.png")
submit_button = Button(image=check_img, highlightthickness=0, command= is_known)
submit_button.grid(column = 1, row =1)


next_card()

window.mainloop()






