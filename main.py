from tkinter import *
# for message box
from tkinter import messagebox
import random
import pyperclip
import json
# -----------------------------SEARCH DATA ----------------------------------------#
def search():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file);
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exists")
    else:
        website = website_entry.get()
        try:
            web = data[website]
        except KeyError:
            messagebox.showinfo(title=website, message="No details for the website exists")
        else:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"\nEmail: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for char in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    # join is used to join strings
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }}
    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave anything empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\n Is it okay to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
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
canvas.create_image(100, 100, image=logo_img, )
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column = 2, sticky="EW")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "jaygandhi129@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

password_btn = Button(text="Generate Password", command=generatePassword)
password_btn.grid(row=3, column=2, sticky="EW")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
