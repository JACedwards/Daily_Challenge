# You are given an array of integers arr, return the length of the longest continuous increasing subarray.
# A continuous increasing subarray is defined as 2 or more consecutive indices such that arr[i] < arr[i+1] .

# Case 1:
# Input: arr = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subarray is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subarray, it is not continuous as elements 5 and 7 are separated by element

# 4.
# Case 2:
# Input: arr = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subarray is [2] with length 1. Note that it must be strictly
# increasing.

#Psuedo code:
    #loop through array
    #checking if num is larger than previous
    #if so, add one to count
    #if not, return count

def longestSub(arr):
    count = 0
    l = 0
    r = 1

    while r <= len(arr)-1:
        if arr[l] < arr[r]:
            count += 1
            l += 1
            r += 1
        else:
            count += 1
            return count
    count += 1
    return count

print(longestSub([1,3,5,4,7]))
