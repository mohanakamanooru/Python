'''
Python Programming   : Object Oriented Programming
Week 8 - Tutorial    : OOP - Coin Flipper

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 17/11/2020

'''
from random import sample


class CoinFlipper:
    num_of_coins=""
    
    def __init__(self,num_of_coins):
        self.num_of_coins = num_of_coins
    
    def flip(self):
        #print(self.num_of_coins)
        rdm_lst = [ sample((True,False),1) for _ in range(0, self.num_of_coins)]
        #print(rdm_lst)
        return rdm_lst
