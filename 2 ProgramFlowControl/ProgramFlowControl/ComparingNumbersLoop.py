# # Python Programming - Comparing Two numbers
# # Mohana Kamanooru 06/10/2020

user_quit = False

while(not user_quit):
    
    # ask the user if he wants to quit if not ask for two numbers,
    num1 = input("Press Q to quit or Enter number 1:")

    if(num1.upper() == "Q"):
        user_quit = True
        break
    else :
        num1 = int(num1)
    
    num2 = int(input("Enter Number 2: "))

    # compare them and then print a message indicating which one is bigger than the other
    if(num1 > num2):
        print(num1, " is greater than ", num2)

    elif(num2 > num1):
        print(num2, " is greater than ", num1)
    
    # (or if they are both the same) with an appropriate message.
    else :
        print("Both numbers are equal")
