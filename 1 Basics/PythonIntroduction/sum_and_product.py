#To create a module to input three integers and print out their sum and product
# Mohana R Kamanooru 01/10/2020

#Read three integer values from the user
value_1 = int(input("Integer 1 :"))
value_2 = int(input("Integer 2 :"))
value_3 = int(input("Integer 3 :"))

#calculate sum and product
total_sum = value_1+value_2+value_3
product = value_1*value_2*value_3

#print the sum and product of the integers
print("The sum is ",total_sum," and the product is ",product)
print("Done!")
