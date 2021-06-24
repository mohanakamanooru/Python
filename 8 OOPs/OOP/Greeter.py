'''
Python Programming   : Object Oriented Programming
Week 8 - Tutorial    : OOP - Greeter

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 17/11/2020

'''


class Greeter:
    name = ""     

    def __init__(self, name):
        self.name = name
     
    def greet_to_screen(self):
        print("Hello,", self.name)
    
    def greet_to_file(self,filename):
        with open(filename, 'a') as welcome_file:
            welcome_file.write("Hello , "+self.name)
 
 
greeter = Greeter("Mohana")
greeter.greet_to_screen()
greeter.greet_to_file("welcome.txt")
