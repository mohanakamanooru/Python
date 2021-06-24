# Python Programming - Program Flow Control
# 
# Mohana R Kamanooru - 08/10/2020
# 
# This python code accepts an input number from the user
# displays "FIZZ" if it is divisible by 3
# displays "Buzz" if it is divisible by 5
# displays "Fizz Buzz" if divisible by both 3 and 5
# displays number itself if not divisible by either

# Ask the user for a number and store it in a variable.
number = int(input("Please enter the number :"))
output = ""

# if the number is divisible by 3, print the message Fizz.
if(number % 3 == 0):
    output = "Fizz"
    
# If the number is divisible by 5, print the message Buzz.
if(number % 5 == 0):
    output += "Buzz"

# if the number is not divisible by either 3 or 5, print the number itself.
elif(output == ""):
    output = number

print(output)

