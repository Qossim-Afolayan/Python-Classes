import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("So play your choice ")

if computer == player:
    print("That's even")

elif computer == choices[0] and player == choices[1]:
    print("Bingo! You won!")

elif computer == choices[1] and player == choices[2]:
    print("That's great! You won!")

elif computer == choices[2] and player == choices[0]:
    print("That's great! You won!")

elif computer == choices[2] and player == choices[1]:
    print("Sorry You lost!")

elif computer == choices[1] and player == choices[0]:
    print("Sorry you lost the game")

elif computer == choices[0] and player == choices[2]:
    print("Sorry You lost the game!")