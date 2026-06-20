"""
Import random statement at the top of the program

"""
import random

def playgame():
    player_choice = input("Player choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = input(random.choice(options))
    print("Thanks for playing")

playgame()



