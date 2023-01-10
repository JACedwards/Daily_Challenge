# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# BONUS: Implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

#brute force because .count() = nested loop? - O(n^2)
# x = [4,1,2,1,2]
# for n in x:
#     if x.count(n) == 1:
#         print(n)


# think this is 0(n^2) too?
#slicing

# def onlyOnce(nums):

#     for i in range(len(nums)):
#         if nums[i] not in nums[i+1:]:
#             return nums[i]

# print(onlyOnce([4,1,2,1,2]))

#dictionary version = O(n)?

def onlyOnce(nums):

    dct = {}


    for n in nums:
        if n in dct:
            dct[n] = 2
        else:
            dct[n] = 1

    for k, v in dct.items():
        if v == 1:
            return k

print(onlyOnce([1]))


