#!/usr/bin/env python3

import random

print("Hello ! Welcome to your fun Rock, Paper, Scissors Game !! You are to choose from Rock, Paper, Scissors and see if you can beat the opponent !")

print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock !")

print("Enter your choice: r for Rock, p for Paper, or s for Scissors")

def user_choices():

    Options = ["r", "p", "s"]
    user_choice = input()

    while user_choice not in Options:
            print("Sorry, this is invalid option. Please Choose from r for Rock, p for Paper, or s for Scissors. Please note, it is case-sensitive.")
            user_choice = input()
    
    return user_choice

def computer_choices():
    return random.choice(["p","r","s"])

def system_check_winner(user_choice, computer_choice):
    if user_choice = computer_choice:
            return "Both sides have tied !"
    elif user_choice == "s":
        return "You beat the opponent !" if computer_choice == "p" else "Sorry you lost !"
    elif user_choice == "r":
        return "You beat the opponent !" if computer_choice == "s" else "Sorry you lost !"
    elif user_choice == "p":
        return "You beat the opponent !" if computer_choice == "r" else "Sorry you lost !"

def main():
    user_choice = user_choices()
    computer_choice = computer_choices()

    print(f"You chose: {user_choice}")
    print(f"Opponent chose: {computer_choice}")

    final = system_check_winner(user_choice, computer_choice)
    print(final)

if __name__ == "__main__":
    main()



