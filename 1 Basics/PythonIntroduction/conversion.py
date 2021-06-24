#Create a module to convert km h-1 to m s-1.
#Your program should ask the user for the speed in km/h
#and then print out its equivalent in m/s.
# Mohana R Kamanooru 01/10/2020

#read input value from user
value_kms = input("Please enter value in Km per hour :")

# 1km/h = 0.2778 m/s
value_ms =0.2778 * float(value_kms)

#print the converted value to scree

print(int(value_ms))
