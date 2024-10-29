#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW10
print("ello orld")
import time
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
num = 5
for i in range(num):
    time.sleep(0.4)
    print (num)
    num -= 1
#2. Create a while loop that prints only even numbers
#between 1 and 30.
for i in range(31):
    if i % 2 == False:
        time.sleep(0.4)
        print(i)
#3. Create a while loop that repeats until the user
#inputs the number 0.
while True:
    for i in range(10):
        print("bazinga")
    ask = input("say 0 if you want to quit")
    if ask == "0":
        break