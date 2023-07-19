import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices).capitalize()
    return computer_choice

def get_user_input():
    valid_choices=["Rock", "Paper", "Scissors"]
    user_choice = input("Rock, Paper or Scissors? ")
    while user_choice.capitalize() not in valid_choices:
        print("Please enter a valid choice")
        user_choice = input("Rock, Paper or Scissors? ")
    return user_choice.capitalize()


def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        return "Its a tie!"
    elif computer_choice == "Rock" and user_choice == "Paper":
        return "You won!"
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return "You lost"
    elif computer_choice == "Paper" and user_choice == "Rock":
        return "You lost"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        return "You won!"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        return "You won!"
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return "You lost"

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_input()
    print(f"Computer picked {computer_choice}")
    print(f"You picked {user_choice}")
    print(get_winner(computer_choice,user_choice))

play_game()
