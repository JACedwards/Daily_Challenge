# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

def findNum(arr, target):
    lower_i = 0
    upper_i = len(arr)-1
    mid_i = 0

    if target not in arr:
        return -1
    while arr[mid_i] != target:
        mid_i = (upper_i + lower_i) // 2
        if arr[mid_i] < target:
            lower_i = mid_i
        else:
            upper_i = mid_i
    
    return mid_i

print(findNum([-1,0,3,5,9,12], 2))