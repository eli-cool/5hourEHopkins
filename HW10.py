#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW10
print("ello orld")
import time
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
num = 5
while num >= 0:
    time.sleep(0.4)
    print(num)
    num -= 1
#2. Create a while loop that prints only even numbers
#between 1 and 30.
num2 = 32
while num2 >= 0:
    time.sleep(0.1)
    print(num2)
    num2 -= 2
#3. Create a while loop that repeats until the user
#inputs the number 0.
while True:
    for i in range(10):
        print("bazinga")
    print("say 0")
    ask = input("if you want to quit")
    if ask == "0":
        break