from tkinter import *
import tkinter.messagebox
import math 
window=Tk()
window.title("Scientific Calculator")
window.geometry("650x400+300+300")
window.resizable(width="False",height="False")

switch= None

def buton0_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"0")

def buton1_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"1")    

def buton2_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"2")    

def buton3_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"3")

def buton4_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"4")

def buton5_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"5")

def buton6_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"6")

def buton7_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"7")

def buton8_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"8")

def buton9_clck():
    if disp.get == "0":
        disp.delete(0,END)
    pos = len(disp.get())
    disp.insert(pos,"9")

def keyevnt(*args):
    if disp.get() == "0":
        disp.delete(0,END)

def butonp_clck():
    pos = len(disp.get())
    disp.insert(pos, "+")

def butond_clck():
    pos = len(disp.get())
    disp.insert(pos, "/")    

def butonm_clck():
    pos = len(disp.get())
    disp.insert(pos, "-")

def butonl_clck():
    pos = len(disp.get())
    disp.insert(pos, "*")

def butonclear_clck(*args):
    disp.delete(0, END)
    disp.insert(0, " ")

def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def arcsin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.asin(ans))
        else:
            ans = math.asin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def arccos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.acos(ans))
        else:
            ans = math.acos(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.degrees(math.atan(ans))
        else:
            ans = math.atan(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def buttonpow_clck():
    pos = len(disp.get())
    disp.insert(pos,"**")

def round_clck():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def logarith_clck():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def fact_clck():
    try:
        ans = float(disp.get())
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def sqrt_clck():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def dot_clck():
    pos = len(disp.get())
    disp.insert(pos, ".")

def pi_clck():
    if disp.get() == "0":
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))

def e_clck():
    if disp.get() == "0":
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))

def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, "(")

def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ")")

def conv_clck():
    global switch
    if switch is None:
        switch = True
        conv_btn["text"] = "Deg"
    else:
        switch = None
        conv_btn["text"] = "Rad" 

def ln_clck():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("ERROR!")

def mod_clck():
    pos = len(disp.get())
    disp.insert(pos, "%")


def btneq_clck(*args):
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except:
        tkinter.messagebox.showerror("ERROR!")

#***************

disp = Entry(window, font="Blue", fg="black", bg="Grey", bd=0, justify=RIGHT, insertbackground="White")
disp.bind("<Return>", btneq_clck)
disp.bind("<Escape>", butonclear_clck)
disp.bind("<Key-1>", keyevnt)
disp.bind("<Key-2>", keyevnt)
disp.bind("<Key-3>", keyevnt)
disp.bind("<Key-4>", keyevnt)
disp.bind("<Key-5>", keyevnt)
disp.bind("<Key-6>", keyevnt)
disp.bind("<Key-7>", keyevnt)
disp.bind("<Key-8>", keyevnt)
disp.bind("<Key-9>", keyevnt)
disp.bind("<Key-0>", keyevnt)
disp.bind("<Key-.>", keyevnt)
disp.insert(0, "0")
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

btnrow1 = Frame(window, bg="Blue")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Arial", relief=GROOVE, bd=0, command=pi_clck, fg="white", bg="Dark Grey")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Arial", relief=GROOVE, bd=0, command=fact_clck, fg="white", bg="Dark Grey")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_btn = Button(btnrow1, text="sin", font="Arial", relief=GROOVE, bd=0, command=sin_clicked, fg="white", bg="Dark Grey")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_btn = Button(btnrow1, text="cos", font="Arial", relief=GROOVE, bd=0, command=cos_clicked, fg="white", bg="Dark Grey")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_btn = Button(btnrow1, text="tan", font="Arial", relief=GROOVE, bd=0, command=tan_clicked, fg="white", bg="Dark Grey")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Arial", relief=GROOVE, bd=0, command=buton1_clck, fg="white", bg="Black")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Arial", relief=GROOVE, bd=0,  command=buton2_clck, fg="white", bg="Black")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Arial", relief=GROOVE, bd=0, command=buton3_clck, fg="white", bg="Black")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Arial", relief=GROOVE, bd=0, command=butonp_clck, fg="white", bg="Dark Grey")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow2 = Frame(window)
btnrow2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(btnrow2, text="e", font="Arial", relief=GROOVE, bd=0, command=e_clck, fg="white", bg="Dark Grey")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Arial", relief=GROOVE, bd=0, command=sqrt_clck, fg="white", bg="Dark Grey")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(btnrow2, text="sin−1", font="Arial", relief=GROOVE, bd=0, command=arcsin_clicked, fg="white", bg="Dark Grey")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(btnrow2, text="cos-1", font="Arial", relief=GROOVE, bd=0, command=arccos_clicked, fg="white", bg="Dark Grey")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(btnrow2, text="tan-1", font="Arial", relief=GROOVE, bd=0, command=arctan_clicked, fg="white", bg="Dark Grey")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)


btn4 = Button(btnrow2, text="4", font="Arial", relief=GROOVE, bd=0, command=buton4_clck, fg="white", bg="Black")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Arial", relief=GROOVE, bd=0, command=buton5_clck, fg="white", bg="Black")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Arial", relief=GROOVE, bd=0, command=buton6_clck, fg="white", bg="Black")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Arial", relief=GROOVE, bd=0, command=buton7_clck, fg="white", bg="Dark Grey")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow3 = Frame(window)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Arial", relief=GROOVE, bd=0, command=conv_clck, fg="white", bg="Dark Grey")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Arial", relief=GROOVE, bd=0, command=round_clck, fg="white", bg="Dark Grey")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Arial", relief=GROOVE, bd=0, command=ln_clck, fg="white", bg="Dark Grey")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Arial", relief=GROOVE, bd=0, command=logarith_clck, fg="white", bg="Dark Grey")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Arial", relief=GROOVE, bd=0, command=buttonpow_clck, fg="white", bg="Dark Grey")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Arial", relief=GROOVE, bd=0, command=buton7_clck, fg="white", bg="Black")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Arial", relief=GROOVE, bd=0, command=buton8_clck, fg="white", bg="Black")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Arial", relief=GROOVE, bd=0, command=buton9_clck, fg="white", bg="Black")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Arial", relief=GROOVE, bd=0, command=butonl_clck, fg="white", bg="Dark Grey")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnrow4 = Frame(window)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Arial", relief=GROOVE, bd=0, command=mod_clck, fg="white", bg="Dark Grey")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Arial", relief=GROOVE, bd=0, command=bl_clicked, fg="white", bg="Dark Grey")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Arial", relief=GROOVE, bd=0, command=br_clicked, fg="white", bg="Dark Grey")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Arial", relief=GROOVE, bd=0, command=dot_clck, fg="white", bg="Dark Grey")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Arial", relief=GROOVE, bd=0, command=butonclear_clck, fg="white", bg="Dark Grey")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="DEL", font="Arial", relief=GROOVE, bd=0, command=butonclear_clck, fg="white", bg="Dark Grey")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Arial", relief=GROOVE, bd=0, command=buton0_clck, fg="white", bg="Black")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Arial", relief=GROOVE, bd=0, command=btneq_clck, fg="white", bg="Dark Grey")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Arial", relief=GROOVE, bd=0, command=butond_clck, fg="white", bg="Dark Grey")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)


window.mainloop()