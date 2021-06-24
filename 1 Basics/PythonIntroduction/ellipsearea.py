#Write a program to calculate and output the area of an ellipse (oval).
#Mohana R Kamanooru 01/10/2020

import math

#read value of major radius from the user
Major_radius = input("Please enter the value of major radius :")

#read value of minor radius from the user
Minor_radius = input("Please enter the value of minor radius :")

#calculate area of ellipse
area=float(math.pi*int(Major_radius)*int(Minor_radius))

#print area of the ellipse
print("Area of the ellipse is ",round(area,2))


