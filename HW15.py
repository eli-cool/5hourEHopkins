#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def helo(num):
    for i in range(int(num)):
        print("hello world")
helo(3)
#2. Create a def function that calculates the average of three numbers.
def calculate(a,b,c):
    return a+b+c / 3


#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def anms(a1,a2,a3,a4,a5):
    print(a3)
    return [a1,a2,a3,a4,a5]

#4. Create a def function that loops from 1 to the number put in the argument.
def loops(num):
    for i in range(1,num+1):
        print("jello wolrd")
#5. Call all of the functions created in 1 - 4 with relevant arguments.
helo(10)
print (calculate(5,5,5))
anms("cow","sheep","donkey","chicken","wendigo")
loops(4)