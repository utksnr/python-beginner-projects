import pyautogui
import tkinter as tk
from tkinter import *
window=tk.Tk()
window.geometry("400x300+50+100")
window.title("artunyavuz")
window.configure(bg="yellow")

def artunyavuz():
    while True:
        pyautogui.write('artunyavuz')
        pyautogui.press("enter")
        

def artunyavuz_buyuk():
    while True:
        pyautogui.keyDown("shift")
        pyautogui.write('artunyavuz')
        pyautogui.press("enter")

def artunyavuz_mors():
    while True:
        pyautogui.write(".- .-. - ..- -. -.-- .- ...- ..- --..")
        pyautogui.press("enter")

def yavuzartun():
    while True:
        pyautogui.write("yavuzartun")
        pyautogui.press("enter")

def yavuzartun_buyuk():
    while True:
        pyautogui.keyDown("shift")
        pyautogui.write("yavuzartun")
        pyautogui.press("enter")

artun=tk.Label(window, text="Artun Yavuz Macro",font="Castellar",bg="yellow",fg="red")
artun.pack()
buton1=tk.Button(window, text="artunyavuz",font="Castellar",command=artunyavuz)
buton1.pack()
buton2=tk.Button(window, text="ARTUNYAVUZ",font="Castellar",command=artunyavuz_buyuk)
buton2.pack()
buton3=tk.Button(window, text=".- .-. - ..- -. -.-- .- ...- ..- --..",font="Castellar",command=artunyavuz_mors)
buton3.pack()
buton4=tk.Button(window, text="yavuzartun",font="Castellar",command=yavuzartun)
buton4.pack()
buton5=tk.Button(window, text="YAVUZARTUN",font="Castellar",command=yavuzartun_buyuk)
buton5.pack()


window.mainloop()