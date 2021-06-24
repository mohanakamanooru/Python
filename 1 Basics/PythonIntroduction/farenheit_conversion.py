#Write a program to convert temperature from fahreheit to celsius
#Mohana R Kamanooru 01/10/2020

#Write a program that prompts the user to input a temperature in Fahrenheit.
#The program will then output the temperature in Celsius.
#The format of the output is required to be:
#         >>> 71 Degrees Fahrenheit is 21.67 degrees Celsius


#read temperature input in F from the user
temp_f= input("Enter temp in Fahrenheit : ")

#[°C] = ([°F] - 32) x 5/9
temp_c= (float(temp_f)-32)*(5/9)



#print the converted temperature in Celsius
print("Temperature in Degrees Clesius is :",temp_c)
    
