# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[i]  is equal to the product of every number in the input array other than input[i].
# Note that you're expected to solve this problem without using division.

# Example 1:
input1 = [5, 1, 4, 2]
# Output: [8, 40, 10, 20]
# Explained:
# 8 == 1*4*2
# 40 == 5*4*2
# 10 == 5*1*2
# 20 == 5*1*4

# Example 2:
input2 = [-5, 2, -4, 14, -6] 
# Output: [672, -1680, 840, -240, 560]

#Pseudo code:

#empty output array
#empty array(s) to collect numbers
#For each index in input, need to Collect integers at index other then index in question
#Need to multiply each the set for each input index
#put products into output array

# Works with import****

import math
def equalProduct(in_arr):
    output = []
    prod = 0



    for i in range(len(in_arr)):
        popped = in_arr.pop(i)
        prod = math.prod(in_arr)
        output.append(prod)
        in_arr.insert(i, popped)
        print(in_arr, output)
    return output

print(equalProduct(input2))


#works without import****

def equalProduct(in_arr):
    output = []
    prod = 1

    for i in range(len(in_arr)):
        popped = in_arr.pop(i)
        print(popped, in_arr)
        for n in in_arr:
            print(n,prod)
            prod = prod * n
            print(prod)        
        output.append(prod)
        in_arr.insert(i, popped)
        print(in_arr, output)
        prod=1
    return output

print(equalProduct([5, 1, 4, 2]))
# Output: [8, 40, 10, 20]