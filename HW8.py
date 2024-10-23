#Name: Eli Hopkins
#Class: 5th Hour
#Assignment: HW8

#1. Print Hello World!
print("Hello World!")
#2. Take the variables below and change the name of the variables to match the type of
#variable they are: string, integer, boolean, or list.

#For example, the first one, Var1 = 4, should be:
#integerVar1 = 4 or intVar1 = 4

#DO NOT CHANGE THE VALUE OF THE VARIABLE.

intVar1 = 4
strVar3 = "Box"
boolVar4 = True
strVar5 = "Nineteen"
strVar6 = "Rope"
intVar7 = 19
strVar8 = "19"
listVar9 = ["Window", "Apple", "Penguin"]
intVar10 = 2
boolVar11 = True
boolVar12 = False
strVar13 = "True"
strVar14 = "False"
listVar15 = [1, 0]
listVar16 = [1]
listVar17 = [0]
intVar18 = 5
strVar19 = "The"
strVar20 = "Game"
intVar21 = 3
intVar22 = 2
intVar23 = 1
listVar24 = ["Liftoff", True]
boolVar25 = boolVar11
boolVar26 = boolVar12
strVar27 = strVar13
strVar28 = strVar14
listVar29 = listVar15
intVar30 = 6
listvars = [intVar1, strVar3, boolVar4, strVar5, strVar6, intVar7, strVar8, listVar9, intVar10, boolVar11, boolVar12, strVar13, strVar14, listVar15,
        listVar16, listVar17, intVar18, strVar19, strVar20, intVar21, intVar22, intVar23, listVar24, boolVar25, boolVar26,
        strVar27, strVar28, listVar29, intVar30]
intsum = 0
#3. Take all the variables you labeled as "integer", add them together, and print the result.
for i in listvars:
    if type(i) == int:  # You can use `type(i) == int` or `isinstance(i, int)` here. Both are valid.
        intsum += i
print(intsum)
