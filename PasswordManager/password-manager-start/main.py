import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

INPUT_WIDTH = 35

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(range(10))
    symbols = ['!', '#', '$', '%', '&', ')', '(', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]\
    + [str(random.choice(numbers)) for _ in range(nr_numbers)]\
    + [random.choice(symbols) for _ in range(nr_symbols)]

    generated_password = "".join(random.sample(password_list, len(password_list)))
    password_entry.insert(END, generated_password)
    pyperclip.copy(generated_password)
    # messagebox.showinfo("Notice", "Password was generated and copied to clipboard. Simply paste into your desired destination")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_input = website_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": username_input,
            "password": password_input,
        }
    }

    def write(data):
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    if len(website_input) == 0 or len(password_input) == 0 or len(username_input) == 0:
        messagebox.showwarning(title="Invalid inputs", message="You still have empty inputs")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered:\nEmail: {username_input}\nPassword: {password_input}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Read old data
                    old_data = json.load(file)
            except FileNotFoundError:
                    write(new_data)
            else:
                # Update old data with new data
                old_data.update(new_data)
                write(old_data)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website_input = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            details = data[website_input]
    except (FileNotFoundError, KeyError) as e:
        messagebox.showerror(title=website_input, message="Password has not been created for this website")
    else:
        email = details["email"]
        password_found = details["password"]
        messagebox.showinfo(title=website_input, message=f"Email: {email} \nPassword: {password_found}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#TODO: Create LOGO
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, columnspan=4)

#TODO: Create INPUT TEXT for 'Website' and 'Email/Username'
website = Label(text="Website:")
website.grid(row=1, column=0)
website_entry = Entry(width=int(INPUT_WIDTH/2))
website_entry.grid(row=1, column=1)
website_entry.focus()

search = Button(text="Search", width=int(INPUT_WIDTH/2-4), command=search)
search.grid(column=2, row=1)

username = Label(text="Email/Username:")
username.grid(row=2, column=0)
username_entry = Entry(width=INPUT_WIDTH)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, string="nguyentvy.37@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=int(INPUT_WIDTH/2))
password_entry.grid(column=1, row=3)

password_generator = Button(text="Generate Password", command=generate_password)
password_generator.grid(column=2, row=3)

add = Button(text="Add", width=INPUT_WIDTH-2, command=add)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
