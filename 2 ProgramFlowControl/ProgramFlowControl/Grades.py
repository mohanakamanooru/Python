# #Python Programming - Grades
# #
# #
# #  Mohana Kamanooru 06/10/2020
# #
# #    Mark	Grade
# #    0	N/S
# #    1-39	F
# #    40-49	D
# #    50-59	C
# #    60-69	B
# #    70-79	A
# #    80-100	A*

# read marks from the user
marks = input("Enter the marks:")

try :
    # if input is not in the range ask user to enter value again
    marks = int(marks)
    if(marks in range(0, 100)):
        # print("Entered value is in the range")
        # print the appropriate grade on the screen
        if(marks == 0):
            print("Your grade is : N/S")
        elif(1 <= marks and marks >= 39):
            print("Your grade is : F")
        elif(1 <= marks and marks >= 39):
            print("Your grade is : D")
        elif(40 <= marks and marks >= 49):
            print("Your grade is : C")
        elif(50 <= marks and marks >= 69):
            print("Your grade is : B")
        elif(70 <= marks and marks >= 89):
            print("Your grade is : A")
        elif(90 <= marks and marks >= 100):
            print("Your grade is : A*")
    else :
        print("entered marks are not between 0 and 100")
    
except:
    print("you have entered wrong input")
    
