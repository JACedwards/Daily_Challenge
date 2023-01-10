# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

#Pseudo:
#  loop through s string:
#  if c == #, pop() form new list
#  else:  append to new list
# repeate with t string
#compare strings, return true if ==

def backspaceEqualCheck(s, t):

    output_s = []

    for c in s:
        if c == '#':
            output_s.pop()
        else:
            output_s.append(c)
    
    print(output_s)

    output_t = []
    for c in t:
        if c == '#':
            output_t.pop()
        else:
            output_t.append(c)
    
    print(output_t)
    if output_s == output_t:
        return True
    return False



print(backspaceEqualCheck(s = "ab##", t = "c#d#"))