''''
Python Programming   : Algorithms
Week 5 - Tutorial    : To implement selection sort algorithm 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 27/10/2020

Algorithm : selection Sort 
'''

def selection_sort(input_list):
    '''
    list: input - accepts integer list as input
    list: output- returns sorted list to the calling function.
    function - sorts the input list in ascending order using 
    selection sort algorithm and return sorted list
    '''
    for ind in range(0,len(input_list)):
        sub_ind = ind 
        for ind2 in range(ind+1,len(input_list)):
            if(input_list[ind2]<input_list[sub_ind]):
                sub_ind = ind2
        temp_var = input_list[ind]
        input_list[ind]= input_list[sub_ind]
        input_list[sub_ind] = temp_var 
    
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
        sorted_list = selection_sort(num_list)
        print ("The sorted list is :" , num_list)
             
