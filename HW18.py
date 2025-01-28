#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["blue", "pink", "green", "red", "orange"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pull():

    if not beanBag:
        print("no more beans!!")
        exit()

    print(beanBag)
    bean = random.choice(beanBag)
    print(bean)
    beanBag.remove(bean)
    redo()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def redo():
    ans = input("would you like to start again? (y/n) ")
    if ans == "y" or "Y":
        pull()
    else:
        exit()
#5. Call the #3 function at the bottom.
pull()