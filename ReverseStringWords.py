# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

#Pseudo:
#Id end of each word (each space)
#reverse each word
#append to list
#covert list back to string

#Works by adding extra space to end of original string

# print(RevWordInPlace("I"))

def RevWordInPlace(s):
    output = []
    r_point = 0
    s = f"{s} "

    for i in range(len(s)):
        if s[i].isspace():
            str_to_rev = s[r_point:i]
            rev_str = str_to_rev[::-1]
            output.append(rev_str)
            r_point = i+1
    output = ' '.join(output)
    print(output)        



print(RevWordInPlace("I"))
