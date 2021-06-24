''''
Python Programming   : Data Processing and Visualisation
Week 6 - Tutorial    : Bar Charts

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 02/11/2020

'''

from numpy.random.mtrand import choice
import matplotlib.pyplot as plt

#declaring constants
#MAX_TOSS_COUNT = 500
MAX_TOSS_COUNT = 50000

if(__name__ == "__main__"):
    
    '''
    Execution of the main program starts here
    '''
    # creating the array with random head and tail
    array_list = [choice (["True", "False"]) for _ in range(0, MAX_TOSS_COUNT)]
    #print(array_list)
    #data_list = []
    data_list = [0 for _ in range(0, MAX_TOSS_COUNT)]
    head_count = 0
    toss = 0
    
    for toss in range(0, MAX_TOSS_COUNT):
        if(array_list[toss] == "True"):
            head_count += 1
            if(toss <= MAX_TOSS_COUNT-1):
                toss += 1
        # print("head_count = " , head_count)
        for ind in range(0, head_count):
            data_list[ind] += 1
        # print(data_list)
        if(toss == MAX_TOSS_COUNT):
                break 
        elif(array_list[toss] == "False"):
            head_count = 0

    occurance = []
    for ind in range(0,MAX_TOSS_COUNT):
        if(data_list[ind] != 0):
            occurance.append(data_list[ind])
        else :
            break
    
    toss_count = [x for x in range(1, len(occurance)+1)]
    print(toss_count)
    print(occurance)
    
    plt.bar(toss_count, occurance)
    plt.show()
