import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("rock, paper, or scissors: ")

    while user_choice not in choices:
        print("Please enter a valid choice.")
        user_choice = input("rock, paper, or scissors: ")
    
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        return "You win"
    else:
        return "Computer wins"

def rock_paper_scissors():
    user_wins = 0
    computer_wins = 0
    play = True

    while play:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You pick {user_choice}")
        print(f"Computer picks {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win":
            user_wins += 1
        elif result == "Computer wins":
            computer_wins += 1

        play_again = input("Do you want to play again? (y/n): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("Invalid input. Please enter 'y' to continue or 'n' to stop: ").lower()
        
        if play_again == 'n':
            play = False
    
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    print("Ending program.")

rock_paper_scissors()
