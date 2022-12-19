import time
from winotify import Notification, audio
from threading import Thread

def Water():
    while True:
        water = Notification(app_id="Health Notification",
                            title="Water",
                            msg="Your reminder to drink water.\nYou didn't drink water for 2 hours!",
                            duration="short",
                            icon="water-bottle.png")

        water.set_audio(audio.Default, loop=False)
        
        water.show()
        time.sleep(7200)
        
def Posture():
    while True:
        posture = Notification(app_id="Health Notification",
                            title="Posture",
                            msg="Your reminder to correct your posture.\nYou should sit straight for your spine health.",
                            duration="short",
                            icon="position.png")

        posture.set_audio(audio.Default, loop=False)
        
        posture.show()
        time.sleep(60*30)

def Takealittlewalk():
    while True:
        walk = Notification(app_id="Health Notification",
                            title="Take A Little Walk",
                            msg="Your reminder to take a little walk.\nYou have been sitting for a long time.\You should take a little walk in your room. ",
                            duration="short",
                            icon="walking.png")

        walk.set_audio(audio.Default, loop=False)
        
        walk.show()
        time.sleep(3600*3)

f1 = Thread(target=Water)
f2 = Thread(target=Takealittlewalk)
f3 = Thread(target=Posture)

f1.start()
f2.start()
f3.start()