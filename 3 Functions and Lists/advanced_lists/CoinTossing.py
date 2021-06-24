'''
Python Programming - advanced lists
@author: Mohana Kamanooru - 15/10/2020
'''
# 0-head, 1-tail
from random import sample


def longest(result_list, cmp_toss):
    #result_list=[['T'],['T'], ['T'], ['T'], ['H'], ['T'], ['H']]
    prev_count = 0 
    current_count = 0    
    for toss in result_list :
        if(toss == cmp_toss):
            current_count += 1
        if(current_count > prev_count):
            prev_count = current_count
        if(toss != cmp_toss):
            current_count = 0

    return prev_count


def t_longest(result_list):
    pass


toss = ('H', 'T')
result_list = []

for x in range(0, 100):
    coin_toss = sample(toss, 1)
    result_list.append(coin_toss)
# print(result_list)    

for x in range(0, 5):
    for y in range (0, 20):
        print(result_list[x + y], end="")
    print()
    
print()

longest_H = longest(result_list, ['H'])
longest_T = longest(result_list, ['T'])

print(" H sequence ", longest_H)
print(" T sequence ", longest_T)

