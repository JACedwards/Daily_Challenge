# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
# 
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# 
# Example 2:
# Input: arr = [1,2]
# Output: false
# 
# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

#Psuedo:
    #Create set of list
    #Loop through set
    # counting how many times each item in set appears in list
    # Append these values to a list
    # Create set of list of frequencies and compare length of set to length of list
    # if they are the same return true
    # else return false

#First version works using double for loop & counter variable

# def uniqueVals(arr):
#     freq = []
#     counter = 0
#     set_arr = set(arr)

#     for n in set_arr:
#         for m in arr:
#             if n == m:
#                 counter += 1
#         freq.append(counter)
#         counter = 0
    
#     return len(set(freq)) == len(freq)

# print(uniqueVals([1,2,2,1,1,3]))


#Second version works using .count(), but time complexity should both be O(n**2)

def uniqueVals(arr):
    freq = []
    set_arr = set(arr)

    for n in set_arr:
        x = arr.count(n)
        freq.append(x)
    
    return len(set(freq)) == len(freq)

print(uniqueVals([1,2]))