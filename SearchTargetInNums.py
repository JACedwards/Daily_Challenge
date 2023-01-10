# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If targetexists, then return its index. Otherwise, return -1.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Brute force

# def search_t(nums, target):

    
#     if target in nums:
#         return nums.index(target)
#     return -1

# print(search_t([-1,0,3,5,9,12], 15))



#***binary search version

def search_t(nums, target):

    hf_len = len(nums) // 2

    l=0
    r=len(nums)-1

    while l<=r:
        mid=r + (l-r)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r-=1
        else:
            l+=1
    return -1

print(search_t([-1,0,3,5,9,12], 17))