'''
Python Programming - advanced lists
@author: Mohana Kamanooru - 15/10/2020

Create a program to throw 2 dice 100 times. Record how often each number from 2 to 12 is
thrown in a suitable list and then print out a graph of your results like so:
Distribution Chart
Score Rolls
2 1 *
3 5 *****
4 11 ***********
5 13 *************
6 15 ***************
7 16 ****************
8 18 ******************
9 8 ********
10 6 ******
11 4 ****
12 3 ***
'''
from random import randint
global OCCURANCE
global ROLL_COUNT

def get_dice_output():
    current_output = randint(1, 6) + randint(1, 6)
    return current_output

def get_occurances():
    for ind in range(0,ROLL_COUNT):
        current_output=get_dice_output()
        if(current_output in range(2,13)):
            OCCURANCE[current_output-2]+=1;
            

def show_graph():
    for x in range(0,len(OCCURANCE)):    
        print(str(x+2).ljust(2)," ",str(OCCURANCE[x]).ljust(2)," ",OCCURANCE[x]*'*')
    #print(sum(OCCURANCE))
    

ROLL_COUNT=100
OCCURANCE=[0]*11
get_occurances()
show_graph()

        
        

    

# get the dice output
# check if the out out put is in the list 