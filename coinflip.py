import random

tailsn =0
headn=0
flips = 0

flip = int(input("How hany times should coin flip: "))

while flips < flip:
    coinvalue = random.randrange(2)
    flips += 1
    if coinvalue == 0:
        tailsn += 1
    elif coinvalue == 1:
        headn +=1
print(f"tails: {tailsn}, heads:{headn}, flips:{flips}")
