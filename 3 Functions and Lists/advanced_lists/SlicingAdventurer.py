'''
Python Programming - advanced lists
@author: Mohana Kamanooru - 15/10/2020

'''
from random import randint

rucksack = ["Water flask", "Cheese", \
               "Gold coins", "Handkerchief", \
               "Tinderbox", "Scrolls", "Dagger", \
               "Rope", "Nuts", "Pipe", "Tobacco", \
               "Wine skin", "Herbs", "Axe"]


def show_rucksack(rucksack):
    for item in rucksack:
        print(item)

    print("Number of items in backpack :", len(rucksack))

    
rucksack.sort()
rucksack.append("Gems")
rucksack.append("Necklace")
rucksack.sort()
show_rucksack(rucksack)

for theft in range(0, 5):
    theft_item=randint(0, len(rucksack)-1)
    print("Stolen Item: ",rucksack[theft_item])
    rucksack.remove(rucksack[theft_item])

show_rucksack(rucksack)

