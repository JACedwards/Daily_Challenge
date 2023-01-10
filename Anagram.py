# Given an array of strings arr, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: arr = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: arr = [""]
# Output: [[""]]

# Example 3:
# Input: arr = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i].length <= 100
# arr[i] consists of lowercase English letters.

#Psuedo:
    # loop through list:
        #create set of each item = w
        #loop through slice of list from item to end of list
            #comparing set version of each item in slice to w
            # if ==:
            # add to temp_list
        #add temp_list to output list
    #return output list

# def isAnagram(arr):

#     temp_list = []
#     output_list = []
#     output = []

#     for i in range(len(arr)):
#         st_w = set(arr[i])
#         for i in range(len(arr)):
#             if st_w == set(arr[i]):
#                 temp_list.append(arr[i])
#         output_list.append(temp_list)
#         temp_list = []

#     for l in output_list:
#         if l not in output:
#             output.append(l)

#     return output


# print(isAnagram(["eat","tea","tan","ate","nat","bat"]))

###Class version####

class Anagrams():

    def __init__(self, arr):
        self.arr = arr

    def isAnagram(self):

        temp_list = []
        output_list = []

        for i in range(len(self.arr)):
            st_w = set(self.arr[i])
            for i in range(len(self.arr)):
                if st_w == set(self.arr[i]):
                    temp_list.append(self.arr[i])
            output_list.append(temp_list)
            temp_list = []
        return output_list

    def removeDups(self):
        output_list = self.isAnagram()

        output = []
        for l in output_list:
            if l not in output:
                output.append(l)

        return output

anagram1 = Anagrams(["eat","tea","tan","ate","nat","bat"])
print(anagram1.removeDups())