#Write a program to calculate and output the square footage of a house
#Mohana R Kamanooru 01/10/2020

#Write a program that asks the user for the width and length of 4 rooms of a house,
#you can assume that the rooms are rectangular (i.e. no alcoves, etc.). Once all the
#information has been collected, the program will then display the square footage per
#room and then the total square footage for the entire house



#read value of width and length from the user
print("Please enter the below values")

Room1_width = input("Rooom1 width :")
Room1_length = input("Room1 Length : ")

Room2_width = input("Room2 width : ")
Room2_length = input("Room2 Length : ")

Room3_width = input("Room3 width : ")
Room3_length = input("Room3 Length : ")

Room4_width = input("Room4 width : ")
Room4_length = input("Room4 Length : ")




#Square footage of Room1,2,3 and 4
Room1_area =  float(Room1_width)*float(Room1_length)
Room2_area =  float(Room2_width)*float(Room2_length)
Room3_area =  float(Room3_width)*float(Room3_length)
Room4_area =  float(Room4_width)*float(Room4_length)

#Totalfootage of the house
Total_area = float(Room1_area+Room2_area+Room3_area+Room4_area)

print("Footage of Room1 : ",round(Room1_area,2))
print("Footage of Room2 : ",round(Room2_area,2))
print("Footage of Room3 : ",round(Room3_area,2))
print("Footage of Room4 : ",round(Room4_area,2))

print("Footage of House is : ",round(Total_area,2))




