#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("GREETINGS EARTHLINGS AHAHAHA")

#2. Create three different boolean variables named Wi-Fi, login, and admin.
wifi = True
login = True
admin = True
#3. Create a separate integer variable that says the number of times
#someone with admin credentials has logged in.
amen = 2
#4. Create a nested if statement that checks to see if Wi-Fi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi:
    if login:
        if admin:
            print("welcome")
            amen += 1
            print(amen, "admins have logged in")
        else:
            print("error you are missing the admin status")
    else:
        print("error you are missing login and admin status")
else:
    print("error you are missing the wifi, login, and admin status")
