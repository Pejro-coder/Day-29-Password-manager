from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_info = website_entry.get()
    email_info = email_username_entry.get()
    password_info = password_entry.get()
    password_confirm_info = password_confirmation.get()

    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Check", message="Please don't leave any fields empty.")
    elif password_confirm_info != password_info:
        messagebox.showinfo(title="Check", message="Passwords don't match.")
    else:
        decision = messagebox.askokcancel(title="Check", message=f"Website: {website_info}\nPassword: {password_info}")

        if decision:
            with open("secret_file.txt", "a") as file:
                file.write(f"{website_info} | {email_info} | {password_info}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Row 1 - Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid()
canvas.grid_configure(row=0, column=0, columnspan=3)

# Row 2 - Website
website_label = Label(text="Website:", anchor='w', width=15)
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website_entry.config(width=35)

# Row 3 - Email/Username
email_username_label = Label(text="Email/Username:", anchor='w', width=15)
email_username_label.grid(column=0, row=2)

email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "peter.stepanic@hotmail.com")
email_username_entry.configure(width=35)

# Row 4 - Password
password_label = Label(text="Password:", anchor='w', width=15)
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3)
password_entry.config(width=25)

password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

# Row 5 - Confirm password
password_confirm_label = Label(text="Confirm password:", anchor='w', width=15)
password_confirm_label.grid(column=0, row=4)

password_confirmation = Entry()
password_confirmation.grid(column=1, row=4)
password_confirmation.config(width=25)

# Row 6 - Add button
add_button = Button(text="Add", width=29, command=save)
add_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
