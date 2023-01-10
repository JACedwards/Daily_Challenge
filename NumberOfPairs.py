# Given an integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
# Example 1:
# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
# Example 2:
# Input: nums = [1,2,3,4], k = 1
# Output: 0
# Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i], k <= 100

#Psuedo:
# if len(set(nums)) != len(nums):
#   return 0

#else
#  slide through nums
#   check first if two nums == each other
#     if not continue
#     if so check if number * each other % 2 = 0
#      if yes, count +=1

def pairOfNums(nums, k):

    if len(set(nums)) == len(nums):
        return 0
    
    count = 0
    r = 0
    l = 1

    while r <= len(nums)-2:
        if nums[r] == nums[l] and (r*l) % k == 0:
            count+=1
            if l == len(nums)-1:
                r+=1
                l = r+1
            else:
                l+=1
        else:
            if l == len(nums)-1:
                r+=1
                l = r+1
            else:
                l+=1

    return count

print(pairOfNums(nums = [3,1,2,2,2,1,3], k = 2))