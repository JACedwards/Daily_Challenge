# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]

# Constraints:
# 1 <= left <= right <= 104

#Pseudo:
    # Use range or enumerate(?) to generate list of numbers from left to right
    # loop through string version of each number in list
        #checking if int version of the number % int version of current character/digit in number = 0
        #If so, append int version of that number to new list

def selfDividing(left, right):

    in_lst_str = []
    in_lst_int = []
    output = []
    i_int = 0
    check = []

    rnge = range(left, right + 1)
    for n in rnge:
        in_lst_int.append(n)
        in_lst_str.append(str(n))

    for string in in_lst_str:
        for c in string:
            if c == '0':
                continue
            else:
                if in_lst_int[i_int] % int(c) == 0:
                    check.append(in_lst_int[i_int])
        i_int +=1

    for i in range(len(check)):
        if check[i] < 10:
            output.append(check[i])
        elif check[i] in check[i+1:]:
            output.append(check[i])
    return output

print(selfDividing(47,85))

# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]