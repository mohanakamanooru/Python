# Python Programming - Comparing Two numbers
# Mohana Kamanooru 06/10/2020

# ask the user for two numbers,
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

# compare them and then print a message indicating which one is bigger than the other
if(num1 > num2):
    print(num1, " is greater than ", num2)

elif(num2 > num1):
    print(num2, " is greater than ", num1)
    
# (or if they are both the same) with an appropriate message.
else :
    print("Both numbers are equal")
