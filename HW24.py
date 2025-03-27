#Name:
#Class: 5th Hour
#Assignment: HW24

import time
from random import randint, choice

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.

characters = []
class Chara:
    def __init__(self,name,health,damage,speed,max_health):
        self.name=name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health
        characters.append(self)
    def hits(self):
        print(self.name,"is getting poisoned!")
        for i in range(10):
            self.health -= randint(1,6)
            print(self.health)
            time.sleep(1)
    def heal(self,heald):
        print(self.name," is healing ",heald.name,"!")
        heald.health += 30
        if heald.health >= 100:
            heald.health = 100
        print(i.health)


#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Chara("warrior",100,20,30,60)
healer = Chara("healer",60,10,30,60)
thief = Chara("thief",50,30,40,50)
mage = Chara("mage",45,35,25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
x = choice(characters)
x.hits()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
for i in characters:
    if i.health != i.max_health:
        healer.heal(i)

