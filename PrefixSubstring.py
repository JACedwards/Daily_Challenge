# You are given a string array
# words
#  and a string
# s, where words[i] and scomprise only of lowercase English letters.
# Return the number of strings in words that are a prefix of s.
# A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.
# Example 1:
# Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
# Output: 3
# Explanation:
# The strings in words which are a prefix of s = "abc" are:
# "a", "ab", and "abc".
# Thus the number of strings in words which are a prefix of s is 3.
# Example 2:
# Input: words = ["a","a"], s = "aa"
# Output: 2
# Explanation:
# Both of the strings are a prefix of s. 
# Note that the same string can occur multiple times in words, and it should be counted each time.

#Pseudo code:
#Using slicing and length of "s":
    #make list of possible prefixes
#check each string in words against list of of possibles
#for each string found increase counter
#return counter

# def prefixSub(words, s):
#     count=0
#     slices=''
#     r=1
#     lst_poss=[]

#     while r <= len(s):
#         slices = s[:r]
#         lst_poss.append(slices)
#         r+=1
        
#     for w in words:
#         if w in lst_poss:
#             count+=1

#     return count


# print(prefixSub(["a","a"], "aa"))


#Class version with internal function call:

class PrefixSubString():

    def __init__(self, words, s):
        self.words = words
        self.s = s

    def prefixSub(self):

        slices=''
        r=1
        lst_poss=[]

        while r <= len(self.s):
            slices = self.s[:r]
            lst_poss.append(slices)
            r+=1
        return lst_poss

    def countSubs(self):

        count=0
        lst_poss = self.prefixSub()

        for w in self.words:
            if w in lst_poss:
                count+=1

        return count


test1 = PrefixSubString(["a","a"], "aa")

print(test1.countSubs())