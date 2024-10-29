#Name: ELi Hopkins
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("hello world")
#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

from random import randint

temp = randint(1,30)

print(temp)

if temp >= 20:
    print("its hot")
else:
    if temp >= 10:
        print("its mild")
    else:
        print ("its cold")

print("thank you")