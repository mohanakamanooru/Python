''''
Python Programming   : Algorithms
Week 5 - Tutorial    : Code to generate list of random numbers with random length

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 27/10/2020

'''
from random import randint
import sys

from Debugging_UnitTesting.BogoSort import bogo_sort
from Debugging_UnitTesting.BubbleSort import bubble_sort
from Debugging_UnitTesting.InsertionSort import insertion_sort
from Debugging_UnitTesting.SelectionSort import selection_sort


# declaring constants
MAX_LIST_SIZE = 20
MAX_RANGE_NUM = 100


def random_list():
    '''
    Returns a list of random numbers with random length
    '''
    # generate a random integer between 0 and 20
    num_count = randint(0, MAX_LIST_SIZE) 
    num_list = []     
    # generate list of random numbers
    for x in range(0, num_count):
        num_list.append(randint(0, MAX_RANGE_NUM))
        
    return num_list


sample_list = random_list()
print(sample_list)
#print(bogo_sort(sample_list))
print(selection_sort(sample_list))
print(insertion_sort(sample_list))
print(bubble_sort(sample_list))      
