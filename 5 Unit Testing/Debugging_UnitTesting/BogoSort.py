''''
Python Programming   : Algorithms
Week 5 - Tutorial    : To implement bogo sort algorithm 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 27/10/2020

Algorithm : bogo Sort 
'''
from random import shuffle


def is_sorted(input_list):
    '''
    input : list of integers
    output: boolean value
    function: returns true if list sorted if not false
    '''
    for ind in range(0, len(input_list) - 1):
        if(input_list[ind] > input_list[ind + 1]):
            return False
        
    return True

        
def bogo_sort(input_list):
    '''
    list: input - accepts integer list as input
    list: output- returns sorted list to the calling function.
    function - sorts the input list in ascending order using 
    bogo sort algorithm and return sorted list
    '''
    while (not is_sorted(input_list)):
        #print(input_list , "Before shuffling")
        shuffle(input_list) 
        #print(input_list , "After shuffling")
    
    return input_list


# Execution of program starts here
if(__name__ == "__main__"):
    while(True):
        try:
            # ask user for the count of numbers to be sorted
            num_count = int(input("Please enter the count of numbers:"))
            num_list = []
                        
            # storing the user entered input integer in a list
            print("Enter the numbers :")
            for x in range(0, num_count):
                num_list.append(int(input()))
                
        except ValueError as e:
            print("Please check the input format.Must be an integer." , e)
            break
        except IndexError as e:
            print("Please check the count again" , e)
            break
        except Exception as e :
            print(e)
        
        # calling the binary_sort function to sort the list 
        sorted_list = bogo_sort(num_list)
        print ("The sorted list is :" , num_list)
             
