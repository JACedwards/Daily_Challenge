# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Esample 1:
# Input: s = "hello"
# Output: "holle"
# Esample 2:
# Input: s = "leetcode"
# Output: "leotcede"


#pseudo:
# Establish variable with vowels as list value
#loop through string, appending vowels to list
#loop through string again, 
#   inserting last vowel in list
#   each time reach vowel in string
#   popping off last vowel in list


def reverseVowels(s):
    vw = ['a', 'e', 'i', 'o','u'] 
    v_only = []
    
    for lt in s:
        if lt in vw:
            v_only.append(lt)

    # print(v_only)
    # print(v_only[-1])

    
    for i in range(len(s)):
        if s[i] in vw:
            s = s[0:i] + v_only[-1] + s[i+1:]
            v_only.pop()
        else:
            continue
    
    return(s)
    
print(reverseVowels("leetcode"))



# Establish variable with vowels as list value
# Map letters of string to their indices
# create list of indices of vowels
# reverse list
# reconstruct string using reversed vowel list/dictionary