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
# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


def backspace(s1, s2):

    lst_1 = list(s1)
    output_1 = []
    
    for c in lst_1:
        if c == '#':
            output_1.pop()
        else:
            output_1.append(c)

    lst_2 = list(s2)
    output_2 = []
    
    for c in lst_2:
        if c == '#':
            output_2.pop()
        else:
            output_2.append(c)

    return output_1 == output_2



print(backspace("a#c", "b"))


