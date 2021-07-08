from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    password_input.delete(0, END)
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

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def show_popup_confirm(inputs):
    if len(inputs['website']) == 0 or len(inputs['password']) == 0:
        return False
    else:
        return messagebox.askokcancel(title=inputs['website'],
                                      message=f"These are the details entered:"
                                              f"\nEmail: {inputs['email']}"
                                              f"\nPassword: {inputs['password']}"
                                              f"\nIs it ok to save?")


def get_input():
    website = website_input_field.get()
    email = email_username_input.get()
    password = password_input.get()
    return {
        "website": website,
        "email": email,
        "password": password,
    }


def clear_inputs():
    website_input_field.delete(0, END)
    password_input.delete(0, END)
    website_input_field.focus()


def save_password():
    inputs = get_input()

    if show_popup_confirm(inputs):
        with open("data.txt", "a") as file:
            for key, data in inputs.items():
                file.write(f"{key}: {data} | ")
            file.write("\n")

        clear_inputs()
    else:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #

# tkinter window set up
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the image from the logo to put on the canvas
password_logo_img = PhotoImage(file="./logo.png")

# create the canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=password_logo_img)
canvas.grid(row=0, column=1)

# create the "website" section
website_label = Label(text="Website:")
website_input_field = Entry(width=35)
# focus cursor on first entry
website_input_field.focus()

website_label.grid(row=1, column=0)
website_input_field.grid(row=1, column=1, columnspan=2, sticky="EW")

# create the "email/username" section
email_username_label = Label(text="Email/Username:")
email_username_input = Entry(width=35)

# insert default email
email_username_input.insert(0, "email@gmail.com")

email_username_label.grid(row=2, column=0)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")

# create the "password" section
password_label = Label(text="Password:", justify=RIGHT)
password_input = Entry(width=21)
generate_password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, sticky="EW")
generate_password_button.grid(row=3, column=2)

# create the "add" button section
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
