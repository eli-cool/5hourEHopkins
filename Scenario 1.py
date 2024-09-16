#Name: Eli Hopkins
#Hour: 5th hour
#Assignment: Scenario 1

# Scenario 1:
# You are a programmer for a fledgling game developer. Your team lead
# has asked you to create a nested dictionary containing five enemy
# creatures (and their properties) for combat testing. Additionally,
# the testers are asking for a way to input changes to the enemy's
# damage for balancing, as well as having it print those changes to
# confirm they went through.

enmy = {
"Enemy1": {
    "Name": "bee",
    "size": "tiny",
    "dmg": "10",
    "Hp": "1",
    "gimmic": "sting"
},
"Enemy2": {
    "Name": "wolf",
    "Size": "medium",
    "Dmg": "50",
    "Hp": "40",
    "gimmic": "howl"
},
"Enemy3": {
    "Name": "bear",
    "Size": "big",
    "Dmg": "50",
    "Hp": "60",
    "gimmic": "tree climb"
},
"Enemy4": {
    "Name": "honey badger",
    "Size": "small",
    "Dmg": "30",
    "Hp": "80",
    "gimmic": "bullet resistant"
},
"Enemy5": {
    "Name": "elephant",
    "Size": "huge",
    "Dmg": "100",
    "Hp": "100",
    "gimmic": "intelligent"}
}

print(enmy)
change = (input("input animal number: "))
dmgchange = (input("input damage change: "))

