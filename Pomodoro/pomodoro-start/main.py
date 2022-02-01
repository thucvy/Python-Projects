from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    checkmark.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_second)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_second)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_second)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = floor(count/60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start()
        mark = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#TODO: "TIMER" LABEL
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50,"normal"))
label.grid(column=1, row=0)

#TODO: IMAGE BACKGROUND
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png") #read through the file and get hold of the image
canvas.create_image(100, 112, image=img)

text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#TODO: "START" AND "RESET" BUTTONS
button_start = Button(text="Start", highlightbackground=YELLOW, command=start)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset)
button_reset.grid(column=2, row=2)

#TODO: CHECK MARK
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()