#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
t = "you tied"
l = "you lose"
w = "you win"
npc = ["rock","paper","scissors"]
def rps():
    while True:
        hand = input("say 1 for rock, 2 for paper, and 3 for scissors ")
        if hand == "1" or hand == "2" or hand == "3":
            break
        else:
            print("retry that")

    if hand == "1":
        hand = "rock"
    elif hand == "2":
        hand = "scissors"
    elif hand == "3":
        hand = "paper"

    npchand = random.choice(npc)
    print(f"you choose {hand}, and they choose {npchand}")

    if hand == "rock":
        if npchand == "rock":
            print(t)
        elif npchand == "scissors":
            print(w)
        elif npchand == "paper":
            print(l)
    elif hand == "paper":
        if npchand == "rock":
            print(w)
        elif npchand == "scissors":
            print(l)
        elif npchand == "paper":
            print(t)
    elif hand == "scissors":
        if npchand == "rock":
            print(l)
        elif npchand == "scissors":
            print(t)
        elif npchand == "paper":
            print(w)
    redo()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def redo():
    ask = input("do you want to restart?(y/n)")
    if ask == "yes" or "y":
        rps()
    else:
        pass
rps()