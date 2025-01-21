#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello():
    print("HELLO hi HII Hey y0 HEYY WOLRD")
#2. Create two empty integer variables named "heads" and "tails"
heads = int()
tails = int()
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip2():
    global heads
    global tails
    for i in range(0,100):
        flip = random.randint(0,1)
        if flip == 1:
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hello();flip2()
#5. Print the final result of heads and tails here
print(heads); print(tails)