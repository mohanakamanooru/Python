''''
Python Programming   : Data Processing and Visualisation
Week 6 - Tutorial    : To show a random scatter plot 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 02/11/2020

'''

from random import randint

import matplotlib.pyplot as plt


if(__name__ =="__main__"):
    '''
    Execution of the main program starts here
    '''
    #creating two array with 10 random numbers
    array_1 = [randint(0,10) for _ in range(0,10)]
    array_2 = [randint(0,10) for _ in range(0,10)]
    
    #Drawing the scatter plot
    plt.scatter(array_1, array_2)
    plt.show()
    
    