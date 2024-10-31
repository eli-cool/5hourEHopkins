#Eli Hopkins
#Class: 5th hour
#Assignment: playground

from random import randint
from time import sleep
#separates 100 into 2 halfs
half = randint (1,48)
half2 = 49 - half
#sets up the points
points = 0
#lives duh
lives = 3

while True:

    askchar = input("would you like to have custom characters? (y/n) ")
    if askchar == "y" or "yes":
        #ask for custom hellos and worlds
        hellos = input("what do you want the citizens to be named?")

    worlds = input("what do you want the hider to be named? say 0 for default ")
    if worlds == "0":
        worlds = "world"

char = []

print("3")
sleep(0.4)
print("2")
sleep(0.4)
print("1")
sleep(0.4)
#a number that keeps track where the World is in the Hellos
total = 0
while True:
#for var half times it prints hello and keeps track what number it currently is on
    for i in range(half):
        total += 1
        print(hellos, total)
#prints world and tottrue takes the number it is on
    total = total + 1
    print (worlds, total)
    tottrue = total
#finishes the hello chain until its 100
    for x in range(half2):
        total = total + 1
        print(hellos, total)
#ask question and checks whether it is tottrue which is the same number world is on
    ans = int(input(f"what number is \"{worlds}\" at? :"))
    if ans == tottrue:
        print("you got it!")
        points = points + 1
        print("your score is", points)
        while True:
            #takes a break and asks you when you want to continue
            a = int(input("say 1 when you want to continue:"))
            if a == 1:
                total = 0
                break
    # if you get the question wrong your lives go down
    else:
        lives = lives - 1
        print("wRooOoNg")
        print("you have", lives, " lives")
        while True:
            a = int(input("say 1 when you want to continue:"))
            if a == 1:
                total = 0
                break
    #death check
    if lives == 0:
        print("you have", lives," lives. YOu lOOsE!")
        print("your score is", points)
        break