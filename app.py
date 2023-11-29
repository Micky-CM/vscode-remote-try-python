#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

print("rock, paper or scissors")


# Create a function so that the user can choose between three options: rock, paper or scissors
def choose_option():
    user_choice = input("Choose rock, paper or scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        choose_option()
    return user_choice

# Create a function so that the computer can choose between three options: rock, paper or scissors
def computer_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice

# create a function so that the user can play again
def play_again():
    user_choice = input("Do you want to play again? (y/n): ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        print("Thank you for playing!")
        exit()
    else:
        print("I don't understand, try again.")
        play_again()

# Create a function so that the user can play the game
def game():
    user_choice = choose_option()
    comp_choice = computer_option()
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
            play_again()
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            play_again()
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            play_again()
    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            play_again()
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")
            play_again()
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            play_again()
    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            play_again()
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            play_again()
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")
            play_again()

# create a function so that the user can see their score at the end of the game
user_score = 0
comp_score = 0

def scores():
    print("Your score is " + str(user_score) + ".")
    print("The computer's score is " + str(comp_score) + ".")


# Run the game
while True:
    game()