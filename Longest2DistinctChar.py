#August 3rd

# Given a string s, return the length of the longest substring that contains at most two distinct characters.
# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

#Pseudo code:
    #Slide through string
    #   with left and right pointers for indices
    #   track number of distinct letters by putting each letter into a list / or f-string
    #       checking if letter already in list/f-string
    #       checking that length of list/fstring is 2 or less
    #   when length exceeds 2 distinct, put string in new list
    #   add 1 to left pointer
    #   and repeat to end of string
    #   check length of strings in output list
    #   return longest string


#turn into class##
class LongestDistinct():

    def __init__(self, s):
        self.s = s
    
    
    def twoDistinct(self):
        
        if len(self.s) < 3:
            return len(self.s)
        
        l = 0
        r = 0
        counter = 0
        st_chk_lst = []
        discrete_strs = []

        while r <= len(self.s)-1:
            #check if new character already in list
            if self.s[r] not in st_chk_lst:
                counter +=1
            if counter <= 2:
                st_chk_lst.append(self.s[r])
                if r == len(self.s)-1:
                    discrete_strs.append(st_chk_lst)
                    r = len(self.s) + 10
                else:
                    r+=1
            elif counter > 2:
                discrete_strs.append(st_chk_lst)
                counter = 0
                st_chk_lst = []
                l += 1
                r = l
            return discrete_strs

    def countLength(self):
        discrete_strs = self.twoDistinct()
        output = []
        output.append(discrete_strs[0])
        discrete_strs = discrete_strs[1:]
        for i in range(len(discrete_strs)):
            if len(discrete_strs[i]) > len(output[0]):
                output.remove(output[0])
                output.append(discrete_strs[i])
        
        return len(output[0])


test1 = LongestDistinct("ccaabbb")
print(print(test1.countLength()))