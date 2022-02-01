from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

entry = Entry(width=10)
entry.grid(row=0, column=1)

label_4 = Label(text="0")
label_4.grid(column=1, row=1)

def calculate():
    result = round(float(entry.get())*1.609344,2)
    label_4.config(text=result)

button = Button(text="Calculate", width=5, command=calculate)
button.grid(column=1, row=2)


window.mainloop()