'''
Python Programming   : List Comprehension, Higher Order Functions , Password Mangling
Week 7 - Tutorial    : List Comprehension 

@author   : Mohana Kamanooru
email     : A0223038@tees.ac.uk
Date      : 02/11/2020

'''
# Given a list of numbers, return a new list but add 3 to each item
from random import randint, shuffle, choice
from string import ascii_lowercase

# creating random list of num
num_list = [num for num in range(0, randint(0, 30))]
shuffle(num_list)
print(num_list)

# adding 3 to every element in the list
new_list = [num + 3 for num in num_list]
print(new_list)

# For the following list, return a new list of all positive numbers, but as integers.
nums = [33.6, -210.1, 55.3, 28.4, -10.2, 77.9, 22.7]

new_nums = [int(num) for num in nums if num > 0]
print(new_nums)

# A list of all numbers divisible by 7 in the range (1 , 100) 
num_div_7 = [ num for num in range(1, 101) if num % 7 == 0]
print(num_div_7)

# For the string An Apple a Day Keeps The Doctor Away, return a list of all capital letters
string_given = 'An Apple a Day Keeps The Doctor Away'
return_string = [ch for ch in string_given if ch == ch.upper() if ch != " "]
print(return_string)

'''
Given a list of strings, create a new list which contains all the palindromes (a word,
phrase, or sequence that reads the same backwards as forwards). You can use the list following list to test:
["civic", "motor", "level", "madam", "hello", "racecar", "python", "rotor"]
'''
palindrome = ["civic", "motor", "level", "madam", "hello", "racecar", "python", "rotor"]
new_palindrome = [ word for word in palindrome if word == word[::-1] ]
print(new_palindrome)

# Given a string, count the number of spaces
string_given = 'An Apple a Day Keeps The Doctor Away'
space_count = len([ ch for ch in string_given if ch == " "])
print(space_count) 

# Given a string, return a new string but remove all the vowels
vowels = 'aeiou'
str_list = ''.join(choice(ascii_lowercase) for i in range(10))
print(str_list)
new_str = ''.join(ch for ch in str_list if ch not in vowels)
print(new_str)

