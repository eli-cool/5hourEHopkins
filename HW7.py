#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("GREETINGS EARTHLINGS AHAHAHA")

#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = False
admin = False
#3. Create a separate integer variable that says the number of times
#someone with admin credentials has logged in.
amen = 0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            print("welcome")
            amen += 1
        else:
            print("error you are missing the admin status")
    else:
        print("error you are missing login and admin status")
else:
    print("error you are missing the wifi, login, and admin status")
