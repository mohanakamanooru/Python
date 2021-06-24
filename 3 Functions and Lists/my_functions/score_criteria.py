'''
Python Programming - demonstrate functions
@author: Mohana Kamanooru - 14/10/2020

'''
from audioop import avg
import math

from my_functions import datafile


def get_grade(dat):
    if(dat >= 70):
        return "Distinction"
    elif(dat >= 60):
        return "Merit"
    elif(dat >= 40):
        return "Pass"
    else:
        return "Fail"


def get_average(dat):
      
    tot_score = 0 
    for ind in range(0, len(datafile.data), 2):
        tot_score += int(dat[ind + 1])
    num_stu = int(len(datafile.data) / 2)
#     print("____________________________________________________")
#     print( "int(len(datafile.data) // 2" , int(len(datafile.data) // 2))
#     print( "int(len(datafile.data) / 2" , int(len(datafile.data) / 2))
#     print("____________________________________________________")
                  
    avg = tot_score / num_stu
    #return format(avg, '.2f')
    return avg


def get_low_score(dat, l_score_ind):
    score_list = []
    for ind in range(0, len(datafile.data), 2):   
        if(dat[l_score_ind] > dat[ind + 1]):
            l_score_ind = ind + 1

    low_list = [dat[l_score_ind - 1], str(dat[l_score_ind])]
    
    return low_list


def get_high_score(dat, h_score_ind):
    
    for ind in range(0, len(datafile.data), 2):        
        if(dat[h_score_ind] < dat[ind + 1]):
            h_score_ind = ind + 1
    h_list = [dat[h_score_ind - 1], str(dat[h_score_ind])]
    
    return h_list


def get_below_avgcount(dat):
    
    average = get_average(dat)
    average = int(math.floor(average))
    avgcount = 0
    for ind in range(0, len(datafile.data), 2):
        if(dat[ind + 1] < average):
            avgcount += 1
            
    return avgcount


def get_above_avgcount(dat):
    
    average = get_average(dat)
    avgcount = 0
    for ind in range(0, len(datafile.data), 2):
        if(dat[ind + 1] >= int(average)):
            avgcount += 1
            
    return avgcount
    
