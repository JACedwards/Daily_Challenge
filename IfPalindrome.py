# Given a string s, return true if a permutation of the string could form a palindrome.

# Example 1:
# Input: s = "code"
# Output: false

# Example 2:
# Input: s = "aab"
# Output: true

# Example 3:
# Input: s = "carerac"
# Output: true

#Psuedo:
#dictionary of letters and number of occurances
#if one letter occurs only onces, remove
#if number of occurances for rest of letters is all even
#True (is pallindrome)

# def isPal(s):
#     hash = {}
#     count = 0
#     ct_1s = []

#     for lt in s:
#         if lt not in hash.keys():
#             count = count + 1
#             hash[lt] = count
#             count=0
#         else:
#             count = hash.get(lt) + 1
#             hash[lt] = count

#     for k, v in hash.items():
#         if len(s) % 2 == 0 and v % 2 != 0:
#             return False
#         else:
#             if v % 2 ==1:
#                 ct_1s.append(1)
#     if len(ct_1s) > 1:
#         return False

#     return True

# print(isPal("carerac"))

#### Class version with internal function call

class IfPal():

    def __init__(self, s):
        self.s = s


    def isPal(self):
        hash = {}
        count = 0
        

        for lt in self.s:
            if lt not in hash.keys():
                count = count + 1
                hash[lt] = count
                count=0
            else:
                count = hash.get(lt) + 1
                hash[lt] = count
        return hash


    def checkTrue(self):
        hash = self.isPal()
        ct_1s = []
        for v in hash.values():
            if len(self.s) % 2 == 0 and v % 2 != 0:
                return False
            else:
                if v % 2 ==1:
                    ct_1s.append(1)
        if len(ct_1s) > 1:
            return False

        return True

pal1 = IfPal("code")

print(pal1.checkTrue())
