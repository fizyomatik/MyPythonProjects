from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, END
from tkinter import  messagebox
import random
import pyperclip


window = Tk()
window.title("Password manager")
window.config(width=600, height=400 ,bg="#9bdeac")


canvas = Canvas(width=200, height=200, bg="#9bdeac", highlightthickness=0)
logo_image= PhotoImage(file="logo.png")

canvas.create_image(100, 100, image = logo_image)
canvas.grid(column = 1, row = 2)


# Functions

def generate_button_func():
    print("generate a password")

# ---------------------------- SAVE ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are details entered: \n Email: {username} \n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password} \n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password +=char

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=3)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=4)

password_label = Label(text="Password:")
password_label.grid(column=0, row=5)


# Buttons
add_button = Button(text="Add", command=save, width=36 )
add_button.grid(column=1, row = 6)

generate_button = Button(text="Generate Password", command=generate_password )
generate_button.grid(column= 3,  row = 5)


# Entries
website_entry = Entry(width=35)
website_entry.grid(column = 1, row = 3)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column = 1, row = 4)

password_entry = Entry(width=35)
password_entry.grid(column = 1, row = 5)




window.mainloop()