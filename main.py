from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

## PANDAS EXTRACTION
try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    og_data = pd.read_csv("french_words.csv")
    unlearn = og_data.to_dict(orient="records")
else:
    unlearn = df.to_dict(orient="records")

card = {}

## FUNCTIONS
def next_card():
    global card, time
    window.after_cancel(time)
    card = random.choice(unlearn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    canvas.itemconfig(card_bg, image=img)
    time = window.after(3000,flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")
    canvas.itemconfig(card_bg, image=img2)

def known():
    unlearn.remove(card)
    data = pd.DataFrame(unlearn)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()


## UI SETUP
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

time = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
img = PhotoImage(file='card_front.png')
img2 = PhotoImage(file='card_back.png')
card_bg = canvas.create_image(400,263,image=img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="wrong.png")
no_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
no_button.grid(column=0, row=1)

tick_image = PhotoImage(file="right.png")
yes_button = Button(image=tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known)
yes_button.grid(column=1, row=1)



next_card()

window.mainloop()