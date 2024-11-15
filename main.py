import json
from json import JSONDecodeError
from textwrap import indent
from tkinter import *
from tkinter import messagebox
import random
from caracters import letters, symbols, numbers
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)


    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}, \nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"Website {website} not found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=27)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()

email_username_label = Label(text="Email/Username")
email_username_label.grid(row=2, column=0)

email_user_entry = Entry(width=27)
email_user_entry.grid(row=2, column=1, pady=5)
email_user_entry.insert(0, "wiliam.gomes99@gmail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1, padx=5, pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, pady=10 )

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2, pady=10)




window.mainloop()