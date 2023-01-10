# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

# Example 1:
# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.

# Example 2:
# Input: n = 6
# Output: 6
# Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.

#Pseudo:
    # first, check to see if "n" is multiple of 2:
        #if so, return n

def smallestInt(n):

    # if n % 2 == 0:
    #     return n

    # return n * 2
    return n if n % 2 == 0 else n*2



print(smallestInt(5))