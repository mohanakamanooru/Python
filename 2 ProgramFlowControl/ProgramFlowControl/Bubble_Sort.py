# Python Programming - Bubble Sort
# Mohana R Kamanooru - 08/10/2020

# Read the count of numbers to be
num_count = int(input('Enter the count of numbers to be sorted :'))
print("Enter ", num_count, " Numbers :")
x = 0
num_list = []

# #Read the input numbers into list
for x in range(0,num_count):
    num_list.append(int(input()))

# repeat comparing for j number of times , i.e., number of elements in list.
for j in range(0, num_count - 1) :
    
    # loop to compare the adjacent elements in the num_list
    for i in range(0, num_count - 1 - j):
        # compare , if i+1th element greater then swap
        if(num_list[i] > num_list[i + 1]) :
            x = num_list[i]
            num_list[i] = num_list[i + 1]
            num_list[i + 1] = x 

# print the sorted list
print(num_list)       
    
