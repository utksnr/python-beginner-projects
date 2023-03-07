from tkinter import *
from cryptography.fernet import Fernet

window = Tk()
window.title ("Encryption and Decryption")
window.geometry("500x400")

key = Fernet.generate_key()
fernet = Fernet(key)

def enc():
    message1 = message.get("1.0",END)
    encmessage = fernet.encrypt(message1.encode())
    final.delete("1.0",END)
    final.insert(END,encmessage)

def dec():
    message2 = message.get("1.0",END)
    message2=bytes(message2,encoding='utf8')
    decmessage = fernet.decrypt(message2).decode()
    final.delete("1.0",END)
    final.insert(END,decmessage)



label1= Label(text="Enter message for encrytion and decryption.")
label1.pack()

message = Text(height=6, width=60)
message.pack()

button1 = Button(text="Encrypt",command=enc)
button1.pack()

button2 = Button(text="Decrypt",command=dec)
button2.pack()


final = Text(height=6, width=60)
final.pack()






window.mainloop()