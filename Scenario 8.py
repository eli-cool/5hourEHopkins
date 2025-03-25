#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: Scenario8
from random import randint

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.


partyDictionary=[]
enmy=[]
class Chara:
    def __init__(self,name,mod,hp,ac,classs,backround,frin=bool):
        self.name=name
        self.mod = mod
        self.hp = hp
        self.ac = ac
        self.frin = frin
        self.backround = backround
        self.classs = classs
        if not backround:
            self.frin = False
        if frin:
            partyDictionary.append(self)
        else:
            enmy.append(self)
#attack functions
    def attk(self,silly):
        print(self.name,"is now attacking",silly.name)
        #hit or miss roll
        roll = randint(1,20) + self.mod
        #check for hit
        if roll >= silly.ac:
            print("HIT!")
            #damage roll
            damage= randint(1,6)+randint(1,6)+self.mod
            silly.hp-=damage
            print(self.name,"did",damage,"DAMAGE!")
        else:
            print("MIIISSSSS")
        #death check
            if not silly.hp > 0:
                print("silly died")
            else:
                print("they LIIVE!")
            #enemy attack back
                enroll = randint(1,20)+silly.mod
                if enroll>=self.ac:
                    print(silly.name,"is attacking",self.name)
                    endamage=randint(1,6)+silly.mod
                    self.hp-=endamage
                    print(silly.name, "did", endamage, "DAMAGE!")
                    #kill check
                    if not self.hp>0:
                        print(silly.name,"died")
                    else:
                        print("ALIVE")
                else:
                    print("MISS!")
        """evil = f"e{silly}"

        print(partyDictionary[str(self)]["Name"], "is attacking a", enmy[evil]["Name"])

        # Hit Roll
        roll = random.randint(1, 20) + partyDictionary[str(self)]["mod"]

        # Check for a Hit

        if roll >= enmy[evil]["AC"]:
            print("HIT!")
            # Damage Roll
            damage = random.randint(1, 6) + random.randint(1, 6) + partyDictionary[str(self)]["mod"]
            enmy[evil]["Hp"] -= damage
            print(f"{partyDictionary[str(self)]['Name']} dealt {damage} damage!")
        else:
            print("MISS!")
        # Check for Enemy Death
        if enmy[evil]["Hp"] <= 0:
            print(enmy[evil]["Name"], "has died!")

        # Enemy Attack Back
        if enmy[evil]["Hp"] > 0:

            enemy_roll = random.randint(1, 20) + enmy[evil]["mod"]
            print(enmy[evil]["Name"], "attacks back!")

            if enemy_roll >= partyDictionary[str(self)]["AC"]:

                print(f"{enmy[evil]['Name']} hits {partyDictionary[str(self)]['Name']}!")
                enemy_damage = random.randint(1, 6) + 2  # Example damage for enemy
                partyDictionary[str(self)]["Health"] -= enemy_damage
                print(f"{enmy[evil]['Name']} deals {enemy_damage} damage!")
            else:
                print(f"{enmy[evil]['Name']} misses!")
        # hero dies check
        if partyDictionary[str(self)]["Health"] < 0:
            print(partyDictionary[str(self)]["Name"], "has died!!")
"""

#(self,mod,hp,ac,classs,backround,frin=bool)
skeleton=Chara("skeleton",7,10,5,(),())
larry=Chara("skeleton",5,17,10,"feral","unknown",True)
skeleton.attk(larry)


