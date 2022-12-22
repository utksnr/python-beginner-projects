import tkinter as tk
from tkinter import *
from langcodes import *
from langdetect import *

mainFrame = tk.Tk()
mainFrame.title("Language Detector")
mainFrame.geometry("500x400")

def lng_detect():
    if text.compare("end-1c", "==", "1.0"):
        label.config(text="Please enter text.")
    else:
        lng = detect(text.get(1.0,END))
        lngname = Language.make(language=lng).display_name()
        label.config(text= (f"Language: {lngname}"))

text = tk.Text(mainFrame,height=15,width=55)
text.pack()

button = tk.Button(mainFrame, text="Detect Language",command=lng_detect)
button.pack()

label = tk.Label(mainFrame, text=" ")
label.pack(pady=10)


mainFrame.mainloop()
