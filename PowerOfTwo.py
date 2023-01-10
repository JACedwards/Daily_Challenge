#August 15


# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: n = 3
# Output: false

import math

def powerTwo(n):

    if n == 0:
        return False

    if (math.sqrt(n)).is_integer():
        return True
    
    for s in range(1, math.floor(math.sqrt(n))):
        if s * s == n:
            return True
    
    return False

print(powerTwo(49))