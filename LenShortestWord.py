# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Added challenge: do this in O(1) space (without making another data structure)
# Example 1:
# s = "Hello World JavaScript!"
# output: 5
# explained: "Hello" and "World" both have 5 characters
# Example 2:
# s = "We built a nest and tested it."
# output: 1
# explained: "a" is the shortest word with a length of 1


#***This solution also works if shortest word is final one in string, whether string ends in punctuation or not!!!!!!!

def shortestString(s):
    c_x = 0
    c_y = 0

    for i in range(len(s)):
        
        if s[i] != " " and i == len(s)-1 and c_x < c_y:
            x = s[i].isalnum()
            if x:
                return c_x+1
            else:
                return c_x
 
        if s[i] != " ":
            c_x+=1
 
        else:
            if c_y == 0:
                c_y = c_x
            else: 
                if c_x < c_y:
                    c_y = c_x

            c_x = 0
    return c_y

print(shortestString("They built nests and so did I"))


#works for period as final character
# def shortestString(s):
#     c_x = 0
#     c_y = 0

#     for i in range(len(s)):
#         if s[i] != " " and i == len(s)-1 and c_x < c_y and s[i] == '.':
#             return c_x
#         if s[i] != " " and i == len(s)-1 and c_x < c_y and s[i] != '.':
#             return c_x + 1   
#         if s[i] != " ":
#             c_x+=1
 
#         else:
#             if c_y == 0:
#                 c_y = c_x
#             else: 
#                 if c_x < c_y:
#                     c_y = c_x

#             c_x = 0
#     return c_y

# print(shortestString("We built nest and tested a"))