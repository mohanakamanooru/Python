'''
Python Programming   : Object Oriented Programming
Week 8 - Tutorial    : OOP - A Class for Math

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 17/11/2020

'''
import sys


class MathEngine:
    num = ""
    
    def __init__(self, num):
        self.num = num
    
    def add(self, num):
        return self.num + num
        
    def sub(self, num):
        return self.num - num

    def mul(self, num):
        return self.num * num

    def div(self, num):
        return self.num / num
    
# ##Testing the class and its methods
# engine = MathEngine(5)
# 
# print(engine.add(5))
# print(engine.sub(5))
# print(engine.mul(5))
# print(engine.div(5))


if __name__== "__main__":
    #program execution starts from here
    while(1):
        #entering the infinite loop here
        try:
            # reading inputs from user
            base_number = int(input("Please enter a base number \n"))
            engine = MathEngine(base_number)
            
            user_option = (input("Select \n A - Addition \n S - Subtraction \n M - Multiplication \n D - Division \n Q - Quit \n")).capitalize()              
            if(user_option not in ('A','S','M','D','Q')):
                raise ValueError("Incorrect option")
            
            num = int(input("Enter Number :"))
                  
            if(user_option == 'A'):
                print(engine.add(num))
                    
            elif(user_option == 'S'):
                print(engine.sub(num))
                    
            elif(user_option == 'M'):
                print(engine.mul(num))
                
            elif(user_option == 'D'):
                print(engine.div(num))
                    
            elif(user_option == 'Q'):
                sys.exit(1)
            
        except ValueError as e:
            print("Error :", e)
    
