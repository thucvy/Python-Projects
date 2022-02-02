from tkinter import *
import pandas as pd
import random

LIGHT_GREEN = "#d8e2dc"
FONT_NAME = "Courier"
random_words = None

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    if count > 0:
        canvas.itemconfig(timer_display, text=count)
        window.after(1000, countdown, count-1)
    else:
        canvas.itemconfig(timer_display, text="")
# ---------------------------- FLIP THE CARD ------------------------------- #

def back():
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_words["English"], fill="white")

# ---------------------------- CREATE NEW FLASH CARD ------------------------------- #
def new():
    global random_words, timer
    window.after_cancel(timer)
    random_words = random.choice(data_dict)
    random_french_word = random_words["French"]
    countdown(3)
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_french_word, fill="black")
    canvas.itemconfig(timer_display, fill="black")
    timer = window.after(3000, back)

# ---------------------------- WHEN CLICK THE RIGHT BUTTON ------------------------------- #
def new_right():
    data_dict.remove(random_words)
    df = pd.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    new()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=70, bg=LIGHT_GREEN)

timer = window.after(3000, back)

# front card
canvas = Canvas(width=800, height=526, bg=LIGHT_GREEN, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 265, image=front_img)
language = canvas.create_text(400, 200, text="Language", font=(FONT_NAME, 30, "italic"))
word = canvas.create_text(400, 300, text="word", font=(FONT_NAME,50,"bold"))
timer_display = canvas.create_text(700, 50, text="", font=(FONT_NAME,50,"normal"))
canvas.grid(row=0, columnspan=2)

#back card
back_img = PhotoImage(file="images/card_back.png")

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightbackground=LIGHT_GREEN, command=new)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightbackground=LIGHT_GREEN, command=new_right)
right_button.grid(row=1, column=1)

# Have the random word appear when start the program
new()

window.mainloop()
