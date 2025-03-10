#Name:Eli Hopkins
#Class: 5th Hour
#Assignment: HW22
from contextlib import nullcontext
from logging import exception, error


#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store():
    def __init__(self,stock,cost,weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def inflation(self):
        newcost = self.cost * 2
        return newcost
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
apple = Store(20,5,85)
clothes = Store(50,30,20)
tv = Store(4,300,800)
#3. Print the stock of all three objects and the cost of the second store item.
print(apple.stock,clothes.stock,tv.stock)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
print(clothes.cost)
print(Store.inflation(clothes))
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
tv.stock /= 4
print(tv.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del apple
try:
    print(apple.weight)
except:
    print("no apple")