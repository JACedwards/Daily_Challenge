# A sequence or series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., where the pattern is: "add 3 to the previous term".
# In this problem, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
# [ 0,  1,    3,      6,   ...]
#   0  0+1  0+1+2  0+1+2+3
# Your Task
# Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. When n < 0 return the sequence with negative terms.
# Examples
#  5  -->  [0,  1,  3,  6,  10,  15]
# -5  -->  [0, -1, -3, -6, -10, -15]
#  7  -->  [0,  1,  3,  6,  10,  15,  21,  28]

#Psuedo:
# 1. create list with [0]
#2. sum = 0?
#3. next digit variable = 1
#  While loop: while len output <= input num + 1:
#  add next digit to count and append to output

def mathSeq(n):

    output = [0]
    sum = 0
    
    if n > 0:
        next_digit = 1
        while len(output) <= n:
            sum = sum + next_digit
            output.append(sum)
            next_digit +=1
    else:
        next_digit = -1
        while len(output) <= abs(n):
            sum = sum + next_digit
            output.append(sum)
            next_digit -=1   

    return output




print(mathSeq(7))