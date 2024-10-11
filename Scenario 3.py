#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: Scenario 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

from random import randint

enmy = {
"e1": {
    "Name": "skeleton",
    "mod": 4,
    "Hp": 13,
    "AC": 14,
},
"e2": {
    "Name":"mummy",
    "mod": 3,
    "Hp": 7,
    "AC": 17,
},
"e3": {
    "Name":"big tongue",
    "mod": 3,
    "Hp": 15,
    "AC": 16,
},
"e4": {
    "Name":"walking cactus",
    "mod": 7,
    "Hp": 6,
    "AC": 12,

},
"e5": {
    "Name": "sphinx",
    "mod": 5,
    "Hp": 17,
    "AC": 10,
}
}
#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).
partyDictionary = {
    "1" : {
        "Name" : "LaeZel",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "mod": 7,
        "Health" : 12,
        "AC" : 17,

    },
    "2" : {
        "Name" : "Shadowheart",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "mod": 2,
        "Health" : 10,
        "AC" : 14,
    },
    "3" : {
        "Name" : "Gale",
        "Class" : "Wizard",
        "Background" : "Sage",
        "mod" : 3,
        "Health" : 8,
        "AC" : 14,
    },
    "4" : {
        "Name" : "Astarion",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "mod": 3,
        "Health" : 10,
        "AC" : 14,
    }
}
#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

def attk(silly, serios):

    evil = f"e{silly}"
    good = serios

    print(good["Name"], "is attacking a", evil["Name"])

    roll = randint(1,20)
    print (good["Name"], "did", roll, "to", evil["Name"])

    evil["Hp"] -= roll

    if evil["Hp"] <= 0:
        print(evil["Name"])

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

print("1 for LaeZel")
print("2 for Shadowheart")
print("3 for Gale")
print("4 for Astarion")

ans = int(input("what character will you use? "))

print("1 for skeleton")
print("2 for mummy")
print("3 for big tounge")
print("4 for walking cactus")
print("5 for sphinx")

ans2 = int(input("which monster will you fight? "))

attk(ans,ans2)

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4




#Party Dictionary Goes Here



#Enemy Dictionary Goes Here



#Combat Code Goes Here