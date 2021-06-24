'''
Python Programming   : Object Oriented Programming
Week 8 - Tutorial    : OOP - Dice Roller

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 17/11/2020

'''
from random import randint
class DiceRoller:
    num_of_dice = ""
    result_list = []
    
    def __init__(self,num_of_dice):
        self.num_of_dice = num_of_dice
    
    def roll(self):
        dice_count = 0
        for _ in range(0,self.num_of_dice):
            dice_count += randint(1,6)
        #print(dice_count)
        return dice_count
    
    def roll_many(self,n):
       # result = [  for _ in range(1,n+1) if(n==1) self.roll() else roll_many(n-1)]
        self.result_list.extend(self.roll())
        self.roll_many(n-1)
        
        
            
        
dice = DiceRoller(1)
#result = dice.roll()
print(dice.roll_many(2))