from tkinter import *
import phonenumbers
from phonenumbers import geocoder
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


window = Tk()
window.title("Phone Number Geolocater")
window.geometry("600x500")

label1 = Label(text="Enter Phone Number")
label1.pack()

def findlocation():
    num = number.get("1.0",END)
    num=phonenumbers.parse(num)
    location = geocoder.description_for_number(num,"en")

    phase1.insert(END,location)

def findlocation2():
    key = "e981fd12c4994c2c9b65fc4254709c7c"
    location=phase1.get("1.0",END)
    geocoder = OpenCageGeocode(key)
    query = str(location)
    res = geocoder.geocode(query)

    lat = res[0]["geometry"]["lat"]
    lng = res[0]["geometry"]["lng"]

    Mmap = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng], popup=location).add_to(Mmap)

    Mmap.save("mylocation.html")

number=Text(height=3)
number.pack()

button = Button(text="Find Location phase1",command=findlocation)
button.pack()

phase1 = Text(height=3)
phase1.pack()

button2 = Button(text="Find Final Location and Save",command=findlocation2)
button2.pack()




window.mainloop()