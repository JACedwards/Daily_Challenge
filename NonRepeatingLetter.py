# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2




#Brute force:
    #For Loop through string by index:
        #if letter in  rest of string (slice)
        #   continue
        #if letter not in rest of string,
            #return indiex of leetter
    #return -1
#Solution 1:

# def nonRepeat(s):
#     for i in range(len(s)):
#         if s[i] in s[i+1:]:
#             continue
#         else:
#             return (i)
#     return -1

# print(nonRepeat("leetcode"))

#solution 1.5: using slices

# woorks! **************  brutish
def nonRepeat(s):
    for i in range(len(s)):
        print(s[i], s[i+1:],  s[:i])
        if s[i] in s[i+1:] or s[i] in s[:i]:
            continue
        else:
            return (i)
    return -1

print(nonRepeat("aabb"))


# Solution 2:  Sliding Window  (doesn't work on some edge cases; doesn't look back)
# def nonRepeat(s):
#     lb=0
#     l=0
#     r=1
#     while r <= len(s)-1:
#         print(s[l], s[r])
#         if s[l] == s[r]:
#             if r+1 == len(s) and s[l] == s[l+1]:
#                 return -1
#             elif r == l+1:
#                 l=r+1
#                 r=l+1
#             else:
#                 l = lb+1
#                 lb+=1
#                 r = l+1
#         else:
#             r+=1
#     return l

# print(nonRepeat("lovevleetcode"))

#VErsion 3:  set to keep track of lookback

