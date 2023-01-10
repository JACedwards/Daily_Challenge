# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


# Example2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

#Pseudo:
#loop through nums 2
#slide through nums 1:
    #if nums 2 n >= slide 1:
    #insert nums2 n
    #pop() nums1


def mergeArrays(nums1,nums2, m, n):

    for x in nums2:
        l = 0
        while l <= (m+ n)-1:
            print(nums1[l])
            if nums1[l] >= x or nums1[l] == 0:
                nums1.insert(l, x)
                nums1.pop()
                l = m + n + 2
            else:
                l+=1
            print(l)
            print(x)
            print(nums1)

    return nums1

print(mergeArrays(nums1 = [1], m = 1, nums2 = [], n = 0))