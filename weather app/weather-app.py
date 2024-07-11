import tkinter as tk
from PIL import ImageTk, Image
import requests
from tkinter import messagebox


def get_weather(city):
    API_key = key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code ==404:
        messagebox.showerror("Error","City not Found")
        return None
    
    weather = res.json()
    icon_id = weather["weather"][0]["icon"]
    temparature = weather["main"]["temp"] - 273.15
    description = weather["weather"][0]["description"]
    city = weather["name"]
    country = weather["sys"]["country"]

    iconUrl = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(iconUrl,temparature,description,city,country)
def search():
    city = cityEntry.get()
    result = get_weather(city)
    if result is None:
        return
    
    result = iconUrl, temparature, description, city, country
    locationLabel.configure(text= f"{city},{country}")

    image = Image.open(requests.get(iconUrl,stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    iconLabel.configure(image=icon)
    iconLabel.image=icon

    tempLabel.configure(text=f"Temparature: {temparature:.2f} C")
    descLabel.configure(text=f"Description: {description}")

root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")

cityEntry = tk.Entry(root, font="Airel, 20")
cityEntry.pack(pady=10)

searchButton = tk.Button(root,text="Search",command=search)
searchButton.pack(padx=10)

locationLabel = tk.Label(root,font="Airel, 40")
locationLabel.pack(20)

iconLabel=tk.Label(root)
iconLabel.pack()

tempLabel = tk.Label(root,font="Airal, 30")
tempLabel.pack()

descLabel = tk.Label(root,font="Airal, 30")
descLabel.pack()
