# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

#psuedo:
    #if len nums == k, return ave of nums
    #slide through nums with slice of k length,
        #checking average of each k-length slice
        #if ave greater than count, replace count with new average
        #return count

# def maxAve(nums, k):

#     if len(nums) <= k:
#         return sum(nums) / k

#     l = 0
#     r = k

#     while r <= len(nums) - 1:
#         ave = sum((nums[l:r])) / k
#         l+=1
#         r+=1

#     return ave

    
# print(maxAve([5], k = 1))

def maxAve(nums, k):

    if len(nums) <= k:
        return sum(nums) / k

    l = 0
    r = k
    ave = 0

    while r <= len(nums) - 1:
        ave = sum((nums[l:r])) / k
        l+=1
        r+=1

    return ave
    
print(maxAve([1,12,-5,-6,50,3], k = 4))