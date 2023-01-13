# Welcome to the first Friday challenge of the New Year! Continuing our theme of sliding window problems this week- a string sliding window problem! Both the first correct response sent and the most efficient response will win an amazon giftcard! To be eligible to win you must not have previously completed the problem.
# Given a string s, find the length of the longest
# substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Pseudo:
#  left pointer 2
#  right pointer 0
#  use slices to check for repeats

def longestUniqueSub(s):

    l = 0
    r = 1
    length = 0
    output = 0

    while r <= len(s)-1:
        if s[r] in s[l:r]:
            length = len(s[l:r])
            if length > output:
                output = length
            l += 1
            r = l + 1
        else:
            r+=1

    return output


print(longestUniqueSub("pwwkew"))