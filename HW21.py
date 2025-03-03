#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
dics = {
    "sport1":{
        "name":"basketball",
        "people":5,
        "ball":True
    },
    "sport2":{
            "name":"football",
            "people":11,
            "ball":True
    },
    "sport3":{
            "name":"fencing",
            "people":2,
            "ball":True
    }
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum

def add(d):
    total=0
    for i in d:
        for x in i.values():
            if isinstance(x,int):
                total+=x
            print(total)

#3. Call the function with arguments here
add(dics)