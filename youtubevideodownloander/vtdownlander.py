from pytube import YouTube
from tkinter import *
from tkinter import filedialog

path=""

def directory():
    global path
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download():
    global path
    link = link_field.get()
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    yt.download(path)

window = Tk()
window.title("Youtube Downloader")
window.geometry("450x200")

path_label = Label(window,text="*********")
path_label.pack()

path_button = Button(window,text="Select Download Location",command=directory)
path_button.pack()


link_field = Entry(window,width=50)
link_field.pack()

download_button= Button(window,text="Download",command=download)
download_button.pack()




window.mainloop()