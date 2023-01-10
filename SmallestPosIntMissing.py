# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

#Psuedo code:
    #find max number in list
    #loop through range from 1 to max number
    #checking if each num in range is in list
    #return first number not in list

#class verion
class MissingSmallInt():

    def __init__(self, nums):
        self.nums = nums
    
    
    def smallestPosMissing(self):
        m = max(self.nums)

        for n in range(1,m+2):
            if n not in self.nums:
                return n

missing1 = MissingSmallInt([7,8,9,11,12])

print(missing1.smallestPosMissing())

#working function version
# def smallestPosMissing(nums):
#     m = max(nums)

#     for n in range(1,m+2):
#         if n not in nums:
#             return n


# print(smallestPosMissing([7,8,9,11,12]))