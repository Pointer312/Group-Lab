#!/usr/bin/env python3

import random

print("Hello! Welcome to your fun Rock, Paper, Scissors Game!! You are to choose from Rock, Paper, Scissors and see if you can beat the opponent!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock!")

def user_choices():
    while True:
        user_choice = input("Enter your choice: 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Sorry, this is an invalid option. Please choose 'r', 'p', or 's'. Please note, it is case-sensitive.")

def computer_choices():
    return random.choice(["p", "r", "s"])

def system_check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Both sides have tied!"
    elif user_choice == "s":
        return "You beat the opponent!" if computer_choice == "p" else "Sorry you lost!"
    elif user_choice == "r":
        return "You beat the opponent!" if computer_choice == "s" else "Sorry you lost!"
    elif user_choice == "p":
        return "You beat the opponent!" if computer_choice == "r" else "Sorry you lost!"

def main():
    while True:
        user_choice = user_choices()
        computer_choice = computer_choices()

        print(f"You chose: {user_choice}")
        print(f"Opponent chose: {computer_choice}")

        result = system_check_winner(user_choice, computer_choice)
        print(result)

        while True:
            re_do = input("Would you like to play again? [y/n]: ").lower()
            if re_do == "y":
                break
            elif re_do == "n":
                print("Sad to see you go. Thank you for playing!")
                return
            else:
                print("Please only type 'y' or 'n'.")

if __name__ == "__main__":
    main()

