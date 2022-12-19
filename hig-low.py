from random import randint

random = randint(0, 100)
guesses = 0
while True:
    guess = int(input(": "))
    if guess > random:
        print("Lower")
    elif guess < random:
        print("Higher")
    else:
        (print(f"You win. ({guesses} guesses used)"), quit())
    guesses += 1