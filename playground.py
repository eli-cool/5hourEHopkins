#Eli Hopkins
#Class: 5th hour
#Assignment: playground
from random import randint

ran = randint (1,48)
ran2 = 49 - ran

total = 0

for i in range(ran):
    total = total + 1
    print("hello", total)

total = total + 1
print ("world", total)
tottrue = total

for x in range(ran2):
    total = total + 1
    print("hello", total)

while True:
    ans = int(input("what number is \"world\" at? :"))
    if ans == tottrue:
        print("you got it!")
        break
    else:
        print("try again")