'''
Python Programming - advanced lists
@author: Mohana Kamanooru - 15/10/2020
'''
from random import randint


def greater_num(num_list):
    l_num =0
    for ind in range(0, len(num_list)):
        if l_num < num_list[ind]:
            l_num = num_list[ind]
    return l_num


def smaller_num(num_list):
    s_num = num_list[0]
    for ind in range(0, len(num_list)):
        if s_num > num_list[ind]:
            s_num = num_list[ind]
    return s_num


def second_largest_num(num_list):
    s_l_num = 0
    l_num = greater_num(num_list)
    for ind in range(0, len(num_list)):
        if(s_l_num < num_list[ind] and num_list[ind] < l_num):
            s_l_num = num_list[ind]
    return s_l_num


def second_smallest_num(num_list):
    s_s_num = num_list[0]
    s_num = smaller_num(num_list)
    for ind in range(0, len(num_list)):
        if(s_s_num >= num_list[ind] and num_list[ind] > s_num):
            s_s_num = num_list[ind]
    return s_s_num


def third_largest_number(num_list):
    th_l_num = 0
    s_l_num = second_largest_num(num_list)
    for ind in range(0, len(num_list)):
        if(th_l_num < num_list[ind] and num_list[ind] < s_l_num):
            th_l_num = num_list[ind]
    return th_l_num


def third_smallest_num(num_list):
    th_s_num = num_list[0]
    s_s_num = second_smallest_num(num_list)
    for ind in range(0, len(num_list)):
        if(th_s_num >= num_list[ind] and num_list[ind] > s_s_num):
            th_s_num = num_list[ind]
    return th_s_num


def num_list_modify(num_list):
    var=(greater_num(num_list),second_largest_num(num_list))
    print("removing   :",var)
    for num in var:
        num_list.remove(num)

def new_modified_list(num_list):
    mod_list=[]
    
    num_list.sort()
    for ind in range(0,int(len(num_list)/2)):
        mod_list.append(num_list[ind])
        
    mod_list.append(50)
    
    num_list.sort()
    for ind in range(int(len(num_list)/2),len(num_list)):
        mod_list.append(num_list[ind])
    
    mod_list.reverse()
    return mod_list


# Main body of the program



num_list = []
for num in range(0, 20):
    num_list.append(randint(0, 99))
#num_list=[99, 60, 67, 57, 7, 62, 58, 2, 19, 61, 1, 42, 10, 61, 50, 61, 16, 75, 55, 53]
print(num_list)
print("Larger Number: ", greater_num(num_list))
print("Smaller Number:", smaller_num(num_list))

print("Second Largest Number: ", second_largest_num(num_list))
print("Second Smallest Number: ", second_smallest_num(num_list))

print("Third Largest Number: ", third_largest_number(num_list))
print("Third Smallest Number: ", third_smallest_num(num_list))

num_list_modify(num_list)
print(num_list)

num_list.sort()
print(num_list)

num_list=new_modified_list(num_list)
print(num_list)