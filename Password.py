import string
import random

import tkinter as tk
from tkinter import ttk
import string
import random


def password(length, numbers=True, symbols=True):
    words = string.ascii_letters
    digits_set = string.digits
    symbols_set = string.punctuation

    characters = words
    if numbers:
        characters += digits_set
    if symbols:
        characters += symbols_set

    password_1 = [random.choice(characters) for char in range(length)]

    # Ensure at least one number if numbers are included
    if numbers and not any(char in digits_set for char in password_1):
        password_1[random.randint(0, length - 1)] = random.choice(digits_set)

    # Ensure at least one symbol if symbols are included
    if symbols and not any(char in symbols_set for char in password_1):
        password_1[random.randint(0, length - 1)] = random.choice(symbols_set)

    return ''.join(password_1)


def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        result_label.config(text="Please enter a valid positive integer for length.", fg='red')
        return

    numbers = include_numbers_var.get()
    symbols = include_symbols_var.get()

    if not numbers and not symbols and length < 1:
        result_label.config(text="Password length must be at least 1.", fg='red')
        return

    generated = password(length, numbers, symbols)
    password_var.set(generated)
    result_label.config(text="Password Generated Successfully!", fg='green')


# Initialize the main window
window = tk.Tk()
window.config(bg='#2C3E50')  # Dark slate background for a sleek look
window.title('PyPassword Generator')
window.geometry('450x450')

# Header Label
header_label = tk.Label(window, text="Password Generator", font=("Times New Roman", 19, 'bold'), bg='#000000',
                        fg='#FFD700')
header_label.pack(padx=10, pady=20)

# Frame for input options
input_frame = tk.Frame(window, bg='#2C3E50')
input_frame.pack(pady=10)

# Password Length
length_label = tk.Label(input_frame, text="Password Length:", font=('Times New Roman', 14, 'bold'), bg='#2C3E50',
                        fg='white')
length_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

length_entry = ttk.Entry(input_frame, width=20)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Include Numbers
include_numbers_var = tk.BooleanVar(value=True)
numbers_check = ttk.Checkbutton(
    input_frame,
    text="Include Numbers",
    variable=include_numbers_var,
    style='TCheckbutton'
)
numbers_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Include Special Characters
include_symbols_var = tk.BooleanVar(value=True)
symbols_check = ttk.Checkbutton(
    input_frame,
    text="Include Special Characters",
    variable=include_symbols_var,
    style='TCheckbutton'
)
symbols_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Generate Button
generate_button = tk.Button(
    window,
    text="Generate!",
    font=('Times New Roman', 15, 'bold'),
    bg='#00BFFF',
    fg='white',
    command=generate_password
)
generate_button.pack(pady=20, ipadx=10, ipady=5)

# Password Display Field
password_var = tk.StringVar()
password_field = ttk.Entry(window, textvariable=password_var, width=30, font=('Courier', 12))
password_field.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=('Times New Roman', 12), bg='#2C3E50', fg='green')
result_label.pack()

# Style configurations for ttk widgets
style = ttk.Style()
style.configure('TCheckbutton', foreground='white', background='#2C3E50', font=('Times New Roman', 12))
style.configure('TEntry', foreground='black')

window.mainloop()




