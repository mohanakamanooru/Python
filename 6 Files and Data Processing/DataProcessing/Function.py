''''
Python Programming   : Data Processing and Visualisation
Week 6 - Tutorial    : To plot a function

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 02/11/2020

'''
import matplotlib.pyplot as plt


def squared(x):
    '''
    This function takes x input integer
    Returns x multiplied by itself 
    '''
    return x * x 
   
#generate a list of numbers from 0 to 1000
num_list = [x for x in range(0,1000)]    
square_list = [squared(int(num)) for num in num_list]
    
#plotting the scatter graph
plt.scatter(num_list , square_list)
plt.show()
    
    
