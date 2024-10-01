#1. Print "Hello World!"
print("hello world yaaay")
#2. Create a list that contains 3 integers
lisp = 68, 42, 102
#3. Create an if statement that prints out whichever of the three numbers is the highest
if lisp[0] > lisp[1] and lisp[0] > lisp[2]:
  print("lisp[0] (68) is the highest")
elif lisp[1] > lisp[0] and lisp[1] > lisp[2]:
  print("lisp[1] (42) is the highest")
elif lisp[2] > lisp[0] and lisp[2] > lisp[1]:
  print("lisp[2] (102) is the highest")
else:
  print("they are all equal")