import tkinter as tk
from tkinter import messagebox
import time

def show_notification():
    title = title_entry.get()
    message = message_entry.get()
    messagebox.showinfo(title=title, message=message)

root = tk.Tk()
root.title("Notification App")

tk.Label(root, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Message:").grid(row=1, column=0)
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1)

notification_button = tk.Button(root, text="Show Notification", command=show_notification)
notification_button.grid(row=2, columnspan=2)

root.mainloop()
