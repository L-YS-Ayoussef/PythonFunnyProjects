from tkinter import *
from tkinter import messagebox
import random
import json  # part 3 --- note 1

field_rows = []  # list of (key_entry, value_entry) for dynamic subfields

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for l in range(nr_letters)]
    password_list += [random.choice(symbols) for s in range(nr_symbols)]
    password_list += [random.choice(numbers) for n in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)   # note 5
    # insert generated password into the last value field (if any)
    if field_rows:
        value_entry = field_rows[-1][1]
        value_entry.delete(0, END)
        value_entry.insert(0, password)

# ---------------------------- UI SETUP ------------------------------- #
# WINDOW
window = Tk()
window.title("LockIt")
window.config(pady=20, padx=20)
window.resizable(False, False)
icon_img = PhotoImage(file="lock.png")
window.iconphoto(False, icon_img)

logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# LABEL
label_main = Label(text="Main field:")     
label_main.grid(row=1, column=0)
label_fields = Label(text="Fields:")       # subfields (key/value)
label_fields.grid(row=2, column=0, sticky="w")

# MAIN ENTRY (generic key)
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1, columnspan=1, padx=0, pady=5)
website_entry.focus()   # note 2

def add_field_row():
    """Add a new subfield row: key + value."""
    row_index = len(field_rows)
    row = 3 + row_index
    key_entry = Entry(width=18)
    key_entry.grid(row=row, column=0, padx=0, pady=2)
    value_entry = Entry(width=25)
    value_entry.grid(row=row, column=1, columnspan=2, padx=0, pady=2)
    field_rows.append((key_entry, value_entry))

# start with a single empty field row
add_field_row()

# SAVE DATA
def save_data():
    website = website_entry.get().strip().lower()

    # collect all non-empty subfields
    fields = {}
    for key_entry, value_entry in field_rows:
        sub_key = key_entry.get().strip()
        sub_value = value_entry.get().strip()
        if sub_key and sub_value:
            fields[sub_key] = sub_value

    if not website or not fields:
        messagebox.showwarning(
            title="Warning",
            message="Please, fill the main field and at least one subfield."
        )
        return

    details_text = "\n".join(f"{k}: {v}" for k, v in fields.items())
    data_dict = {website: fields}

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered\n{details_text}\n\nIs it ok to save?"
    )
    if is_ok:
        try:
            with open("data.json", "r") as data:
                content = json.load(data)
                content.update(data_dict)
        except FileNotFoundError:
            content = data_dict

        with open("data.json", "w") as data:
            json.dump(content, data, indent=4)

        website_entry.delete(0, END)
        for key_entry, value_entry in field_rows:
            key_entry.delete(0, END)
            value_entry.delete(0, END)

# FIND WEBSITE
def find_website():
    website = website_entry.get().strip().lower()
    if not website:
        messagebox.showinfo(title="OOPS!", message="Please enter a main field name to search for.")
        return

    try:
        with open("data.json", "r") as data:
            all_content = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS!", message="No DATA")
        return

    if website in all_content:
        fields = all_content[website]
        details = "\n".join(f"{k}: {v}" for k, v in fields.items())
        messagebox.showinfo(title=website, message=details)
    else:
        messagebox.showinfo(title="OOPS!", message="No entry found with this name!")


# BUTTON
add = Button(text="Add", width=30, bg="blue", command=save_data)
add.grid(row=10, column=1, columnspan=1, pady=10)
search = Button(text="Search", width=14, bg="orange", command=find_website)
search.grid(row=1, column=2, padx=0, pady=5)

add_field_btn = Button(text="Add field", width=14, bg="orange", command=add_field_row)
add_field_btn.grid(row=2, column=1, padx=0, pady=5, sticky="w")


window.mainloop()
# FUTURE FEATURE IN THIS PROGRAM --->
"""
CHECK ON THE WEBSITE NAME. IF IT IS EXIST AND THE USER INPUTTED IT,
ASK THE USER IF HE WANTS TO CHANGE ANY OF THE DATA STORED IN THE JSON FILE 
"""
