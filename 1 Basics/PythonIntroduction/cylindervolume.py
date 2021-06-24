#Write a program to calculate and output the volume of a cylinder.
#Mohana R Kamanooru 01/10/2020

import math

#read value of radius from the user
radius = input("Please enter the value of radius :")



#calculate area of ellipse
volume=float(math.pi*pow(int(radius),3))

#print volume of the Cylinder
print("Volume of Cylinder ",round(volume,2))
