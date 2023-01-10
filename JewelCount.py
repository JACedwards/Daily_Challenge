# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

from ensurepip import version
from itertools import count


# Pseudo:
#     Loop through stones, 
#     Checking if each is in jewels
#     if so, increase count

# def jewelCount(jewels, stones):

#     count = 0
#     for s in stones:
#         if s in jewels:
#             count += 1
#         else:
#             continue
#     return count

# print(jewelCount("z", "ZZ"))

# List comprehension version

def jewelCount(jewels, stones):

    return len([s for s in stones if s in jewels])

print(jewelCount("aA", "abbbAa"))
