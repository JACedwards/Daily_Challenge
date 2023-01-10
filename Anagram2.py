# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

#Psuedo: do with while loop to minimize possible time complexity
# compare lengths, if != False
#  while r-pointer <= len of t-1:
#    if t[l-pointer] not in s,
#          return false
#    else:
#     remove that letter from s
#     rppointer +=1

def anagram(t, s):
    if len(t) != len(s):
        return False
    for l in t:
        if l not in s:
            return False
        else:
            s.replace(l, '', 1)
    return True


print(anagram(s = "rat", t = "car"))
