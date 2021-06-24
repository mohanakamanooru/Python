'''
Python Programming   : List Comprehension, Higher Order Functions , Password Mangling
Week 7 - Tutorial    : List Comprehension 

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 02/11/2020

'''
import copy
 
 
# creating a dictionary 
weekdays = {'1' : 'monday', 
    '2' :'tuesday',
    '3' :'wednesday',
    '4' :'thursday',
    '5' :'friday',
    '6' :'saturday',
    '7' :'sunday'}
 
new_days = copy.deepcopy(weekdays)
 
#iterate through the dictionary 
for day in new_days :
    print(day)
     
    if(day == '1'):
        print( weekdays.pop(day))
 
 
print(weekdays)
print(new_days)
