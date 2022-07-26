"""This program is a rock  paper scissors python game.
For this program, we will have one user and the other will be the computer.
When the user gives an input the computer randomly makes a choice.

Inputs = The user enters a choice (rock, paper, scissors)
Output = The program displays computers choice

Rock smashes Scissors
Paper wraps Rock
Scissors cuts Paper
It is a tie when both the user and the computer makes the same choice. """

import random

input("Welcome to Rock,Paper,Scissors!, press enter to start ")

user_score = 0
computer_score = 0

while True:
    print()
    choices = [ "rock", "paper", "scissors"]

    computer_action = random.choice(choices)
    user_action = None

    while user_action not in choices:
        user_action = input("rock, paper, or scissors?: ").lower()

    if user_action == computer_action:
        print("computer: ",computer_action)
        print("player: ",user_action)
        print("Tie!!, You think like a computer")

    elif user_action == "rock":
        if computer_action == "paper":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print("Paper wraps rock,You lose):, the computer read your mind")
            computer_score += 1
        if computer_action == "scissors":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print("Rock smashes scissors,You win!!!(: (:, the computer wants revenge ")
            user_score += 1

    elif user_action == "paper":
        if computer_action == "scissors":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print(" Scissors cuts Paper,You lose):, the computer read your mind")
            computer_score += 1
        if computer_action == "rock":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print(" Paper wraps Rock You win!!!(: (:, the computer wants revenge ")
            user_score += 1
    elif user_action == "scissors":
        if computer_action == "rock":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print("Rock smashes Scissors, You lose):, the computer read your mind")
            computer_score += 1
        if computer_action == "paper":
            print("computer: ", computer_action)
            print("player: ", user_action)
            print("Scissors cuts Paper, You win!!!(: (:, the computer wants revenge ")
            user_score += 1

    print("You have",user_score,"wins")
    print("The computer has",computer_score,"wins")
    print()

    play_again = input("Do you have what it takes to go again? (yes/no): ").lower()
    while play_again != "no" and play_again != "yes":
        play_again = input("Invalid input, please try again: ").lower()

    print("\n-----------------------------------------------------\n")

    if play_again == "no":
        break