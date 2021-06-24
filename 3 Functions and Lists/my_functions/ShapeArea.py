'''
Python Programming - demonstrate functions
@author: Mohana Kamanooru - 08/10/2020

'''
# write functions that calculate 
# area of a sphere, cylinder and cone.
from math import pi, sqrt


# define an empty function
def First_empty():
    pass


# function sphere(r) - int inputs , float output rounded to 2decimals
# input - radius r as input
# output - returns area of sphere
def sphere(r):
    area_sphere = pi * pow(r, 2)
    output= round(area_sphere, 2)
    return output

# function cylinder(r,h)- int inputs , float output rounded to 2decimals
# input - radius r and height h 
# output - returns area of cylinder
def cylinder(r, h):
    area_cylinder = (2 * pi * r * h) + (2 * pi * pow(r, 2))
    return round(area_cylinder, 2)


# function cone(r,h) - int inputs , float output rounded to 2decimals
# input - radius r and height h
# output - returns area of cone
def cone(r, h):    
    l = sqrt((r * r) + (h * h))
    area_cone = pi * pow(r, 2) + (pi * r * l)
    return round(area_cone, 2)

# Main body of program.
# write the program to calculate area using the functions 
print("Please select the shape")
shape = input("Sphere  :    1 \nCylinder:    2 \nCone    :    3\nQuit    :    q")

while(shape not in ['1', '2', '3', 'q']):
    shape = input("Select correct type :")
    
if(shape.lower() == '1'):
    radius = input("Enter radius :")
    print(sphere(int(radius)))
    
elif(shape.lower() == '2'):
    radius = input("Enter radius :")
    height = input("Enter height :")
    print(cylinder(int(radius), int(height)))

elif(shape.lower() == '3'):
    radius = input("Enter radius :")
    height = input("Enter height :")
    print(cone(int(radius), int(height)))
    
elif(shape.lower() == 'q'):
    print("Quitting  - Program Ended")

