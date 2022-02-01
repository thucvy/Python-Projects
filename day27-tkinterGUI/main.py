import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=600, height=500)
window.config(padx=200, pady=200)

#Label
my_label = tkinter.Label(text="I am label", font=("Arial",24,"bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    # my_label["text"] = "Button was clicked!"
    # my_label.config(text="Button was clicked")
    my_label.config(text=input.get())

#Button
button = tkinter.Button(text="Click ME!", command =button_clicked)
button.grid(column=1, row=1)

#Another Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
#Entry
input = tkinter.Entry(width=10)
input.grid(column=3,row=2)







window.mainloop()