import pywhatkit as pwt
from tkinter import *

window=Tk()
window.title=("Text to Hand Writing")
window.geometry("600x500")

label1 = Label(text="Ender Your Text")
label1.pack()

def change():
    txt = text.get("1.0",END)
    pwt.text_to_handwriting(txt,"handwritingtext.png",[60,220,60])

text= Text(height=6)
text.pack()

button = Button(text="Enter",command=change)
button.pack()


window.mainloop()