from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/cantonese_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer first
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Cantonese", fill="black")
    cantonese_word = f"{current_card['cantonese']} ({current_card['pronunciation']})"
    canvas.itemconfig(card_word, text=cantonese_word, fill="black")
    canvas.itemconfig(card_sentence, text="")
    canvas.itemconfig(card_jyutping, text="")
    canvas.itemconfig(card_meaning, text="")
    canvas.itemconfig(card_background2, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="grey")
    canvas.itemconfig(card_word, text=current_card["english"], fill="grey")
    canvas.itemconfig(card_sentence, text=current_card["sentence"], fill="grey")
    canvas.itemconfig(card_jyutping, text=current_card["jyutping"], fill="grey")
    canvas.itemconfig(card_meaning, text=current_card["meaning"], fill="grey")
    # Why this background does not change
    canvas.itemconfig(card_background2, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background2 = canvas.create_image(400, 263, image=card_front_img)
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_sentence = canvas.create_text(400, 363, text="", font=("Ariel", 20))
card_jyutping = canvas.create_text(400, 423, text="", font=("Ariel", 20))
card_meaning = canvas.create_text(400, 393, text="", font=("Ariel", 20))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
