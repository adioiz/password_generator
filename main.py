from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- SEARCH ------------------------------- #
def search_password():
    try:
        with open('data.json', "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops..", message="No data file found")
    else:
        if web_entry.get().capitalize() in data:
            email = data[web_entry.get().capitalize()]["email"]
            password = data[web_entry.get().capitalize()]["password"]
            messagebox.showinfo(title=web_entry.get().capitalize(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops..", message=f"No details for {web_entry.get().capitalize()} exists.")
        
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [random.choice(letters) for _ in range(random.randint(3, 5))]
    password_sym = [random.choice(symbols) for _ in range(random.randint(2, 3))]
    password_num = [random.choice(numbers) for _ in range(random.randint(2, 3))]

    password_list = password_let + password_sym + password_num
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        web_entry.get().capitalize(): {
            "email": username_entry.get(),
            "password": pass_entry.get(),
        }
    }
    if len(web_entry.get()) == 0 or len(username_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="Oops...", message="Please make sure you have'nt left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(), message=f"These are the details entered: \nEmail/username: {username_entry}\nPassword: {pass_entry}\nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json', "r") as data_file:
                    data = json.load(data_file) # reading old data
            except FileNotFoundError:
                with open('data.json', "w") as data_file:
                    json.dump(new_data, data_file, indent=4) # saving the updated data
            else:
                data.update(new_data) # updating old data with new data
                with open('data.json', "w") as data_file:
                    json.dump(data, data_file, indent=4) # saving the updated data
            finally:
                web_entry.delete(0, "end")
                username_entry.delete(0, "end")
                pass_entry.delete(0, "end")

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels and inputs

website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(column=0, row=1)
username_label = Label(text="Email/username:", font=(FONT_NAME, 10))
username_label.grid(column=0, row=2)
pass_label = Label(text="Password:", font=(FONT_NAME, 10))
pass_label.grid(column=0, row=3)
add_button = Button(text="Add", width = 33, command=save)
add_button.grid(column=1, row=4, columnspan=2)
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)
search_pass_button = Button(text="Search", command=search_password, width = 14)
search_pass_button.grid(column=2, row=1)
# inputs

def temp_text(e):
    # delete the begining text in the input box
    username_entry.delete(0, "end")

web_entry = Entry(bg="white", width=28)
web_entry.grid(column=1, row=1)
web_entry.focus()

username_entry = Entry(bg="white", width=28) 
username_entry.insert(0, "adi.oizerovich@gmail.com")
username_entry.grid(column=1, row=2)
username_entry.bind("<FocusIn>", temp_text)

pass_entry = Entry(bg="white", width=28) 
pass_entry.grid(column=1, row=3)


window.mainloop()