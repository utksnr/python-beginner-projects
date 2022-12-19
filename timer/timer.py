from time import sleep

duration = int(input("Please enter duration in times: "))

c = 0
while c < duration:
    print(c, end="\r")
    sleep(1)
    c += 1

print("Time is up.")    