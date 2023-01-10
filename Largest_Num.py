# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.


# Example 1:
nums1 = [5,7,3,9,4,9,8,3,1]

# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

# Example 2:
nums2 = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

# #***Learned Counter import from Sven

# # from collections import Counter

# # def largestNum(nums):
# #     output=[]
# #     x = Counter(nums)
# #     print(x)

# #     for k, v in x.items():
# #         if v == 1:
# #             output.append(k)

# #     if output == []:
# #         return -1

# #     return max(output)

# # print(largestNum(nums2))


# #Dylan's solution:

# def biggestOne(alist):
#     counts={}
#     for num in alist:
#         print(num)
#         counts[num] = counts.get(num,0)+1
#         print(counts)
#     ones=[k for k in counts if counts[k] == 1]
#     return max(ones) if ones else -1

# biggestOne([9,9,8,8])

# Nate's:

def largestUniqueNumber(arr):
        unique = set()
        dup = set()
        for i in arr:
            if i not in unique:
                unique.add(i)
            else:
                dup.add(i)  
        print(unique, dup)
        res = unique - dup
        print(res)
        if res:
            return max(res)
        return -1

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))