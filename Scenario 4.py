#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: Scenario 4
from random import randint
#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
from time import sleep

while True:
    ask = int(input("how many players?"))
    if ask > 0:
        break
colgate = {}

for i in range(1,ask +1):

    ran = randint(1, 4)
    if ran == 1:
        ran = "red"
    elif ran == 2:
        ran = "blue"
    elif ran == 3:
        ran = "yellow"
    elif ran == 4:
        ran = "green"
    print("the model is ",ran)

    while True:
        rate = int(input("rate the model from 1 to 5 "))
        if ask > 0:
            break

    colgate.update({ran:rate})

hiest = max(colgate.values())

toothmaxing = next(iter(colgate))
max_key = 0
for i in colgate:
    if colgate[i] > colgate[toothmaxing]:
        max_key = i

print("the average ratings for all models rated is ",sum(colgate.values()) / len(colgate.values()))
print("the highest ranked model is ",hiest,"and their color was ",max_key)


