#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)

except:
    print("hello world")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    inp=int(input("input a number that divides 100 "))
    print(100/inp)
except ZeroDivisionError:
    print("no")
#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    int=int(input("number "))
    print(int)
except ValueError:
    print("no")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.

num = 6

while True:
    num-=1
    if num <0:
        raise Exception("zero error")
    print(num)