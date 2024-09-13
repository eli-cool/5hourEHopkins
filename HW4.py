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
print(dic["abc"][1])
#update function to add a fourth key to the dictionary with a value
dic.update({"updated key":"updated value"})
#print entire dictionary
print(dic)
#clear all data inside the dictionary then print
dic.clear()
print(dic)
#make a nested dictionary with three entries containing the name
#of another classmate and two other pieces of information within each entry

classroom = {
"student1": {
    "Name": "Eli",
    "Age": "16",
    "fav color": "Green",
    "fav Game": "Terraria",
},
"student2": {
    "Name": "Ethan",
    "Age": "17",
    "fav color": "Blue",
    "fav Game": "Eldenring",
},
"student3": {
    "Name": "Ryley",
    "Age": "17",
    "fav color": "Green",
    "fav Game": "Skyrim",
}
}

#print the names of all three classmates on the same line
print(classroom["student1"]["Name"],classroom["student2"]["Name"],classroom["student3"]["Name"])