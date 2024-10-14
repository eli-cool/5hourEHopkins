#Eli Hopkins
#Class: 5th hour
#Assignment: playground

from random import randint

ran = randint (1,48)
ran2 = 49 - ran

points = 0

lives = 3

total = 0
while True:

    for i in range(ran):
        total = total + 1
        print("hello", total)

    total = total + 1
    print ("world", total)
    tottrue = total

    for x in range(ran2):
        total = total + 1
        print("hello", total)

    ans = int(input("what number is \"world\" at? :"))
    if ans == tottrue:
        print("you got it!")
        points = points + 1
        print("your score is", points)
        while True:
            a = int(input("say 1 when you want to continue:"))
            if a == 1:
                total = 0
                break
    else:
        lives = lives - 1
        print("wRooOoNg")
        print("you have", lives, " lives")

        while True:
            a = int(input("say 1 when you want to continue:"))
            if a == 1:
                total = 0
                break

    if lives == 0:
        print("you have", lives," lives. YOu lOOsE!")
        print("your score is", points)
        break