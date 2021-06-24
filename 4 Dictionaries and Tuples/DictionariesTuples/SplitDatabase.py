''''
Python Programming   : File Operations and tuples
Week 4 - Tutorial    : To learn writing to, reading from, appending to and deleting from files. 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 20/10/2020

1Write a script that will read in the car database used in question 3 
and write out 3 files named as make_model_year.txt containing information 
about one car only. For example, mitsubishi_outlander_2015.txt should contain:
Mitsubishi
Outlander
2015

'''
import sys 

# from DictionariesTuples import properties
# from DictionariesTuples.properties import CARS_COUNT

# declaring Constants
# FILE = properties.FILE
# CARS_COUNT = properties.CARS_COUNT
FILE = "cars_excercise.txt"


# declaring variables
vehicle_list = {}
car = {}



def create_write_file():
    '''
    function: creates a filename with make_model_year.txt format
    and writes the contents into the file
    '''
    for ind in range(0, CARS_COUNT):
        temp = vehicle_list[ind]
        file_name = temp.get("Make") + "_" + temp.get("Model") + "_" + temp.get("Year") + ".txt"
        print(file_name)
        with open(file_name, "w") as file:
            file.write(temp.get("Make") + "\n")
            file.write(temp.get("Model") + "\n")
            file.write(temp.get("Year"))
                
    return


def read_file(filename):
    '''
    str: input - takes filename as input
    function: reads the file and stores in a directory 
    dict : vehicle_list - contains the information from file in dict format
    '''
    global CARS_COUNT
    try:
        with open(filename , "r")as car_info :
            CARS_COUNT = int(sum(1 for line in open(filename,"r"))/3)
            
            print(CARS_COUNT)
            for count in range(0, CARS_COUNT):
                car = {
                    "Make" : car_info.readline().replace("\n", ""),
                    "Model" : car_info.readline().replace("\n", ""),
                    "Year" : car_info.readline().replace("\n", ""),
                }
                vehicle_list[count] = car
    except  FileNotFoundError as e :
        print("File not found ", e)
        sys.exit(1)
    return 


# Execution of main program 
if(__name__ == "__main__"):
    try:
        # read from a file and store in the file_list
        read_file(FILE)
        create_write_file()
            
    except FileNotFoundError as e:
        print("Program Terminated ,", e)
        sys.exit(1)
    
