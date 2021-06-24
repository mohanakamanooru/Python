# Python Programming - Sorting
# Mohana Kamanooru 06/10/2020

# ask the user for three numbers 
first_num = int(input("Enter the first number :"))
second_num = int(input("Enter the second number :"))
third_num = int(input("Enter the third number :"))

values_sorted = False

# if num1>num2, then swap 1 and 2 and compare with num3
while(not values_sorted):
    
    if(first_num <= second_num and second_num <= third_num):
        values_sorted = True

    elif(first_num > second_num):
        temp = first_num
        first_num = second_num
        second_num = temp

    elif(second_num > third_num):
        temp = third_num
        third_num = second_num
        second_num = temp
    
print(first_num, ",", second_num, ",", third_num)

