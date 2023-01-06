"""1/2/2023 -- Day 0 of Learning to Code -- Finished Setting Up VS Code"""


"""1/3/2023 -- Day 1 of Learning to Code -- Practice Scenarios"""

#Scenario 1 START
#practicing if/else statemnts, UDF's, and variables
x = 1
false = "x = under 1"
true = "x = equal to or over 1"

def if_else_practice():
    if x >= 1:
        print(true)
    else:
        print(false)

#if_else_practice()
#Scenario 1 END

#Scenario 2 START
#practicing integrating variables and text in print statments 
age = 20
name = "Grayson"

def drinking():
    if age >= 21:
        print("You can go in" + name + ".")
    else:
        print("I'm sorry, " + name + ", you are underage.")

#drinking()
#Scenario 2 END

#Scenario 3 START
#distinguishing return vs print statment nomenclature 
def sum_function(num1, num2):
    sum_variable = num1 + num2
    return sum_variable

#print(sum_function(6,6))
#Scenario 3 END


"""_______ -- Day 2 of Learning to Code -- _______"""
#OBJECTIVES: (1) turtle project (2) return vs print (3) better comment writing 