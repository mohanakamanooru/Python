''''
Python Programming   : Data Persistance, Dictionaries, Tuples
Week 4 - Tutorial    : To learn writing to, reading from, appending to and deleting from files. 

@author       : Mohana Kamanooru
email         : A0223038@tees.ac.uk
Date          : 20/10/2020

'''
import os
import sys
from pip._vendor.distlib.compat import raw_input

# constants
MENU_LIST = []


def check_menu(user_input):
    '''
    str input - user requested sandwich name 
    str output - availability and selection
    function - checks if the input value is available in the file and returns respective results
    '''
    load_menu_list()
    output = ""    
    for item in MENU_LIST:
        if(user_input in item.casefold()):
            output += item.replace("\n", ",")
        
    if(output == ""):
            return "Sorry, Requested item is not available" 
    else:
        return output + " is/are available"


def load_menu_list():
    '''
    output - list with the menu items from the list
    function - open and read the menu text file and store menu items into list
    '''
    # print(os.getcwd())
    try:
        with open ("menu.txt", "r") as menu_file:
            for line in menu_file:
                MENU_LIST.append(line)
    except FileNotFoundError as fe :
        print("Menu File is not found/available")
        sys.exit(1)
    return

    
if (__name__ == "__main__"):
    # program execution starts from here
    try:
        # Ask the user for the name of sandwich
        user_input = raw_input("Please enter the sandwich you wish for: ")
        #print(check_menu.__doc__)
        
    except (IndexError or ValueError) as e:
        print("Entered input is not valid ", e)
        sys.exit(1)
    
    
    # Check if the user input is available i the menu or not
    print(check_menu(user_input.casefold()))

