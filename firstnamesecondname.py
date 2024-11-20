while True:
    fullname=input("Enter your full name: ")
    fullname=fullname.strip()

    nspace = fullname.count(" ")

    if nspace == 1:
        break
    else:
        print("Invalid input. Please enter your full name.")

spaceindex = fullname.index(" ")

firsname = fullname[:spaceindex]
secondname = fullname[spaceindex+1:]

newform = firsname.capitalize() + " " + secondname.capitalize()

print("Your name is: ", newform)
