import time
import tkinter as tk
from tkinter import messagebox

def remind_to_drink_water():
    last_drink_time = time.time()
    minutes_to_remind = 60

    while True:
        current_time = time.time()
        minutes_since_last_drink = (current_time - last_drink_time) / 60

        if minutes_since_last_drink >= minutes_to_remind:
            messagebox.showinfo("Drink Water Reminder", "It's been an hour! Time to drink water.")
            last_drink_time = current_time

        time.sleep(60)

def main():
    root = tk.Tk()
    root.withdraw()

    remind_to_drink_water()

main()
