# Write a program to calculate and output the area of a circle.
# Write Python code in your module to ask the user for the radius of a circle.
# The program will then calculate, store and output the area of the circle to the user
# Mohana R Kamanooru 01/10/2020

import math

#read value of radius from the user
radius = input("Please enter the value of radius :")

#calculate area of circle
area=float(math.pi*pow(int(radius),2))

#print area of the circle
print("Area of the circle is ",round(area,2))

#calculate circumference of circle
circum=float(math.pi*(int(radius)*2))

#print area of the circle
print("Circumference of the circle is ",round(circum,2))

