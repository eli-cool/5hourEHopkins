#Name: Eli Hopkins
#Hour: 5th hour
#Assignment: HW4

#print helllo world
print("Hello World")
#create dictionary with 3 keys
#one key has a list for a value with 3 numbers
dic = {
    "batman": "joker",
    "mario": "bowser",
    "abc": [1,2,3]
}
#print value of one of the three numbers by itself
print(dic["abc"[1]])
#update function to add a fourth key to the dictionary with a value
dic.update({"updated key":"updated value"})
#print entire dictionary
print(dic)
#clear all data inside the dictionary then print
dic.clear()
print(dic)
#make a nested dictionary with three entries containing the name
classroom = {
"Eli": {
    "Age": "16",
    "fav color": "Green",
    "fav Game": "Terraria",
},
"Ethan": {
    "Age": "17",
    "fav color": "Blue",
    "fav Game": "Eldenring",
},
"Ryley": {
    "Age": "17",
    "fav color": "Green",
    "fav Game": "Skyrim",
}
}
#of another classmate and two other pieces of information within each entry

#print the names of all three classmates on the same line