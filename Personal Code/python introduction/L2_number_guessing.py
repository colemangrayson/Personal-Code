"""Practicing interactive programs"""
#Altered program to include a function and add the ability for redo's

import random

#VARIABLES
the_answer = random.randint(0,10)

#CODE 
while True:
    guess = int(input("Pick a number: "))         
    if guess == the_answer:
        print("Correct!")
        break
    else:
        print("Incorrect. Try Again.")