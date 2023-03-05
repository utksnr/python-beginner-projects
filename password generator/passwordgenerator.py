import random
from tkinter import *
from tkinter.ttk import *

def main():
    entry.delete(0,END)

    password_length = var1.get()

    easy = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    hard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, password_length):
            password = password + random.choice(easy)
        return password
    
    elif var.get() == 0:
        for i in range(0,password_length):
            password = password + random.choice(medium)
        return password
    
    elif var.get() == 3:
        for i in range(0,password_length):
            password = password + random.choice(hard)
        return password
    
def generate():
    password1 = main()
    entry.insert(10, password1)

window = Tk()
var = IntVar()
var1 = IntVar()

window.title("Password Generator")

Random_password = Label(window, text="Password")
Random_password.grid(row=0)
entry = Entry(window)
entry.grid(row=0, column=1)
    
c_label = Label(window, text="Length")
c_label.grid(row=1)

button = Button(window, text="Generate", command=generate)
button.grid(row=0, column=3)

reasy = Radiobutton(window, text="Low", variable=var, value=1)
reasy.grid(row=1, column=2, sticky='E')
rmedium = Radiobutton(window, text="Medium", variable=var, value=0)
rmedium.grid(row=1, column=3, sticky='E')
rhard = Radiobutton(window, text="Strong", variable=var, value=3)
rhard.grid(row=1, column=4, sticky='E')
combo = Combobox(window, textvariable=var1)

combo["values"] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")

combo.current(0)
combo.bind("selected")
combo.grid(column=1, row=1)

window.mainloop()