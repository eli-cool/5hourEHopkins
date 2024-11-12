#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
lisp = [4,7,2,9,3,13,6,53,29,20]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
evenlist = []
oddNumbers = 0
oddlist = []
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in lisp:
    if i % 2:
        evenlist.append(i)
        evenNumbers += 1
    else:
        oddlist.append(i)
        oddNumbers += 1

empty = ()
# Print the total count of even and odd numbers.
print (evenNumbers, "even numbers")
print (evenlist)
print (oddNumbers)
print (oddlist, "odd numbers")