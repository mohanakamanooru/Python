# Small example of applying mangling rules to "password"
# James Fairbairn 02/03/2020
# # Modified 2020 MK
# #
# # **DO NOT REMOVE THIS HEADER**
# #
# # Notes:
# #   + This file is for demonstration purposes only.
# #   + You must use this example to guide your own solution.
# #     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**


def capitalise(base):  # NB the correct UK Spelling
    return [base.capitalize()]


def up(base):
    return [base.upper()]


def replace_a(base):
    return [base.replace('a', '@')]


def append_num(base, start=0, end=20):
    return [base + str(num) for num in range(start, end)]


# added def @Mohana Kamanooru
def replace_a4(base):
    return [base.replace('a', '4')]


# added def @Mohana Kamanooru
def replace_s(base):
    return [base.replace('s', '$')]


def replace_s5(base):
    return [base.replace('s', '5')]


def replace_o(base):
    return [base.replace('o', '0')]


def leet_a_s(base):
    return [base.replace('a', '')]


def leet_o(base):
    return [base.replace('o', '')]


def leet_replace_ss(base):
    return [base.replace('ss', 's')]


def leet_replace_pword(base):
    return [base.replace('ass', '')]

# replace every even char
#

def leet_replace_r(base):
    return [base.replace('r', '')]


base = "password"
# base = "pass"

# Yes, this is a list of FUNCTIONS - it's allowed, they're objectsq
# test_rules = [replace_a, up, append_num, capitalise]
test_rules = [replace_a, up, append_num, capitalise, replace_a4, replace_s,
replace_s5, replace_o, leet_a_s, leet_o, leet_replace_ss, leet_replace_r, leet_replace_pword]

permutations = [base]

for rule in test_rules:
    new_permutations = []
    for perm in permutations:
        # extend - appends the contents of a seq to the list
        new_permutations.extend(rule(perm))  # note the recursion
    permutations.extend(new_permutations)

print(permutations)
pwd_list = [ word for word in permutations if word == 'pswd']
print(pwd_list)

# how are duplicated handled
print(len(permutations))

