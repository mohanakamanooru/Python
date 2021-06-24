# #Python Programming
# #Read the list of number from user
# #calculate the sum of numbers in the even indices
# #
# #Mohana Kamanooru 06/10/2020
# #
# #
# #

# size=int(input("Enter the count of numbers in the list"))
num_list = [14, 5, 19, 20, 21, 66, 89]
total = int(0)
var = int(0)

while(var <= len(num_list)):
    if(var % 2 == 0):
        total += num_list[var]        
    var += 1

# #while( var <= len(num_list)):
# #    sum+=num_list[var]
# #    var=var+2
    
print("Sum of values at even indices : ", total)
               
