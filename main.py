from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD_COLOR = "#91C2AF"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
TIMER_SEC = 3000
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/italian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_word()


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    word_label.config(text=current_card["Italian"], bg="white", fg="black")
    canvas.itemconfig(canvas_image, image=card_front)
    language_label.config(text="Italian", fg="black", bg="white")
    flip_timer = window.after(TIMER_SEC, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    language_label.config(text="English", fg="white", bg=BACK_CARD_COLOR)
    word_label.config(
        text=current_card["English"], fg="white", bg=BACK_CARD_COLOR)


# Window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIMER_SEC, flip_card)

# Canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button = Button(
    image=wrong_img, command=next_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = Button(
    image=right_img, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=1)

# Labels
language_label = Label(text="Italian", font=LANGUAGE_FONT, bg="white")
language_label.place(x=400, y=150, anchor=CENTER)

word_label = Label(font=WORD_FONT, bg="white")
word_label.place(x=400, y=263, anchor=CENTER)

next_word()

window.mainloop()
