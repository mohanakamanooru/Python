#Write a program to calculate and output the square footage of a house
#Mohana R Kamanooru 01/10/2020

#Write a program that asks the user for the width and length of 4 rooms of a house,
#you can assume that the rooms are rectangular (i.e. no alcoves, etc.). Once all the
#information has been collected, the program will then display the square footage per
#room and then the total square footage for the entire house



#read value of width and length from the user
print("Please enter the below values")

Room1_width = input("Rooom1 width : ")
Room1_length = input("Room1 Length : ")
Room1_height = input("Room1 height : ")

Room2_width = input("Room2 width : ")
Room2_length = input("Room2 Length : ")
Room2_height = input("Room2 height : ")

Room3_width = input("Room3 width : ")
Room3_length = input("Room3 Length : ")
Room3_height = input("Room3 height : ")

Room4_width = input("Room4 width : ")
Room4_length = input("Room4 Length : ")
Room4_height = input("Room4 height : ")


#volume Room1,2,3 and 4
Room1_volume =  float(Room1_width)*float(Room1_length)*float(Room1_height)
Room2_volume =  float(Room2_width)*float(Room2_length)*float(Room2_height)
Room3_volume =  float(Room3_width)*float(Room3_length)*float(Room3_height)
Room4_volume =  float(Room4_width)*float(Room4_length)*float(Room4_height)

#Totalfootage of the house
Total_volume = float(Room1_volume+Room2_volume+Room3_volume+Room4_volume)

print("Volume of Room1 : ",round(Room1_volume,2))
print("Volume of Room2 : ",round(Room2_volume,2))
print("Volume of Room3 : ",round(Room3_volume,2))
print("Volume of Room4 : ",round(Room4_volume,2))

print("Volume of House is : ",round(Total_volume,2))




