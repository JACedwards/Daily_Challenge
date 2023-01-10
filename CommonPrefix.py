# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Pseudo
# compare first character in strings 2 and 3 to first in string 1:
    #if not all ==, return ""
#loop through indices
    #if all 3 are ==,
        #continue
    #else:
        #return slice [:i]
        # add that letter to output string
        #
# Works unless entire word is shared

def comPrefix(strs):
    if strs[0][0] != strs[1][0] or strs[0][0] != strs[2][0]:
        return "empty string"
    for i in range(len(strs)):
        if strs[0][i] == strs[1][i] and strs[0][i] == strs[2][i]:
            continue
        else:
            return strs[0][0:i]

print(comPrefix(["flower","flow","flight"]))



