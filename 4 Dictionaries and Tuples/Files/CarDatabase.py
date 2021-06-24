''''
Python Programming   : File Operations and tuples
Week 4 - Tutorial    : To learn writing to, reading from, appending to and deleting from files. 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 22/10/2020

'''
import sys 

def read_input_car():
    '''
    function: asks user to for the make model and year of the car 
    dict: output - return dictionary with user given values
    '''
    
    input_car = {"Make": input("Enter Make    :"), \
              "Model": input("Enter Model   :"), \
              "Year": input("Enter Year    :")}
    
    return input_car


def update_file(vehicle_dict, user_action): 
    '''
    dict,str: input - takes two parameters, dict and string (add or del)
    function: for del opens a file and overwrites with vehicle_dict 
                for add action, opens file in append mode and adds vehicle_dic to file.
    '''  
      
    if(user_action == "del"):
        with open(FILE, 'w')as car_info :        
            for vehicle in vehicle_dict:
                car_info.write(vehicle_dict[vehicle].get("Make") + "\n")
                car_info.write(vehicle_dict[vehicle].get("Model") + "\n")
                car_info.write(vehicle_dict[vehicle].get("Year") + "\n")
    
    elif(user_action == "add"):
        with open(FILE, 'a')as car_info :        
            car_info.write(vehicle_dict.get("Make") + "\n")
            car_info.write(vehicle_dict.get("Model") + "\n")
            car_info.write(vehicle_dict.get("Year") + "\n")
    
    return


def read_file(FILE):
    '''
    str: input - takes filename as input
    function: reads the file and stores in a directory 
    dict : output - contains the information from file in dict format
    '''    
    try:
        car_info_list=[]
        with open(FILE , "r")as car_info :
            for line in car_info :
                car_info_list.append(line.replace("\n",""))
                
            for ind in range(0,len(car_info_list),3):
                car ={"Make":car_info_list[ind],"Model" : car_info_list[ind+1],"Year" : car_info_list[ind+2],}
                key = car.get("Make") +'dict'
                vehicle_dict.update({key : car })
                
                
#             cars_count = int(len(FILE) / 3) - 1          
#             for count in range(0, cars_count):
#                 car = {
#                     "Make" : car_info.readline().replace("\n", ""),
#                     "Model" : car_info.readline().replace("\n", ""),
#                     "Year" : car_info.readline().replace("\n", ""),
#                 }
#                 key = car.get("Make") +'dict'
#                 vehicle_dict.update({key : car })
                
        #print(vehicle_dict.items())
    except  FileNotFoundError as e :
        print("File not found ", e)
        sys.exit(1)
        
    return vehicle_dict


def add_new_car(vehicle_dict):
    '''
    function: asks user to input new car details and then 
    adds this new car to the existing vehicle_dict directory
    '''
    # print("Adding New Car")
    new_car = read_input_car()
        
    key = new_car.get("Make") +"dict"
    vehicle_dict.update({key: new_car})
    
    update_file(new_car, "add")

    return


def remove_car(vehicle_dict):
    '''
    function: asks user to input car details to remove and then 
    removes this new car to the existing vehicle_dict directory
    '''
    # print("Removing Car")
    del_car = read_input_car()
    
    for vehicle in vehicle_dict :
        listed_car = vehicle_dict[vehicle]
        # to check if listed car is same as the 
        if((listed_car.get("Make") == del_car.get("Make"))and \
           (listed_car.get("Model") == del_car.get("Model")) and \
           (listed_car.get("Year") == del_car.get("Year"))):
            
            # Ask user to reconfirm deletion
            del_confirm = input("Confirm deletion (y/n):")
            if(del_confirm == 'y'):
                # if reconfirms deletion then rewrite file
                vehicle_dict.pop(vehicle)
                update_file(vehicle_dict, "del")
                return
    print("No such entry found in database")
    return 


# declaring Constants
FILE = "cars_info.txt"
vehicle_dict = {}

# Execution of main program 
if(__name__ == "__main__"):
    # starting an infinite loop, runs until user quits
    while(True):
        try:
            # read from a file and store in the vehicle_dict
            print("Choose an option below")
            user_action = input("Add new car: A\nRemove car : R\nQuit  : Q")            
        except Exception as e:
            print("Program Terminated ,", e)
            sys.exit(1)
        
        #if user wants to quit
        if(user_action.casefold() == 'q'):
            print("Thank You")
            sys.exit(1)
            
        #loading the data file into dict
        vehicle_dict = read_file(FILE)
        
        #if user wants to remove a car, calling the remove function
        if(user_action.casefold() == 'r'):
            remove_car(vehicle_dict)
         
        #if user wants to add a car, calling add car function   
        elif(user_action.casefold() == 'a'):
            add_new_car(vehicle_dict) 
        
        #if no condition is true, assuming user input is incorrect      
        else :
            print("Invalid input. Exiting App")
            sys.exit(1)
        
