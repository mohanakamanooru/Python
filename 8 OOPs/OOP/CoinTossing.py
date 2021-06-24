'''
Python Programming - advanced lists
@author: Mohana Kamanooru - 15/10/2020
'''
# 0-head, 1-tail
from CoinFlipper import CoinFlipper


def longest(result_list, cmp_toss):
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

coin = CoinFlipper(100)
result_list = coin.flip()
print(result_list)

longest_True = longest(result_list, [True])
longest_False = longest(result_list, [False])

print(" True sequence ", longest_True)
print(" False sequence ", longest_False)

