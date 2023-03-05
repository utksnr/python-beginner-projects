from tkinter import *

window = Tk()
window.title("Wight Converter")

def convert():
    gram = float(label2_value.get())*1000
    miligram = float(label2_value.get())*1000000
    ton = float(label2_value.get())/1000
    pound = float(label2_value.get())*2.20462
    ounce = float(label2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    t4.delete("1.0",END)
    t4.insert(END, miligram)
    t5.delete("1.0", END)
    t5.insert(END, ton)

label1 = Label(window, text="Input the weight in KG")
label2_value = StringVar()
label2 = Entry(window, textvariable=label2_value)
label3 = Label(window, text="Gram")
label4 = Label(window, text="Pound")
label5 = Label(window, text="Ounce")
label6 = Label(window, text="Miligram")
label7 = Label(window, text="Ton")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
t4 = Text(window, height=5, width=30)
t5 = Text(window, height=5, width=30)

button = Button(window,text="Convert",command=convert)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
label5.grid(row=1, column=2)
label6.grid(row=1, column=3)
label7.grid(row=1, column=4)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
t5.grid(row=2, column=4)
button.grid(row=0, column=2)

window.mainloop()
