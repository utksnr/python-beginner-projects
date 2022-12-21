import tkinter as tk
from tkinter.font import Font
import customtkinter
mainFrame = customtkinter.CTk()
mainFrame.geometry("400x400")
mainFrame.title("Daily Cigarette Counter")
mainFrame.resizable(height="False", width="false")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
count=0
time= 0



def countplus():
    global count
    count = count + 1
    cigarcounter.configure(text=(f"You smoke {count} cigarette today."))

def life():
    global time
    global count
    time = (count*11)
    cigarcounter.configure(text=(f"{count} cigarettes cost you {time} mins of your life."))

#***************

cigarcounter=customtkinter.CTkLabel(master=mainFrame,
                               text=(f"You smoke {count} cigarette today."),
                               width=120,
                               height=40,
                               fg_color=("white", "blue"),
                               corner_radius=8)
cigarcounter.place(x=115 ,y=50)

button=customtkinter.CTkButton(master=mainFrame,
                               text="+1 button",
                               command=countplus)

button.place(x=135,y=150)

resultbuton=customtkinter.CTkButton(master=mainFrame,
                               text="Click to see lost lifetime.",
                               command=life)
resultbuton.place(x=130,y=200)


#**************







mainFrame.mainloop()