# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

#Pseudo:
    #Turn array into integer
    #Add 1
    #Turn integer into array

#Craig's

# def largeInt(arr):
#     string = ""
#     list_output = []
#     for n in arr:
#         string = string + str(n)
#     integer = int(string)
#     integer += 1
#     integer = str(integer)
#     for c in integer:
#         list_output.append(c)
#     return list_output

# print(largeInt([1,2,3]))

#list comprehension version
def largeInt(arr):
    string = ""
    list_output = []

    for n in arr:
        string = string + str(n)  
    string = str(int(string) + 1)
    list_output = [int(c) for c in string]

    return list_output

print(largeInt([1,2,3]))

#Fellow Alumns'

# def increment_array(arr):
#     test = [str(x) for x in arr]
#     print(test)
#     joi  = ''.join([str(x) for x in arr])
#     print(joi, type(joi))
#     fstring = f"{''.join([str(x) for x in arr])}+1"
#     print(fstring, type(fstring))
#     arr_as_int = eval(f"{''.join([str(x) for x in arr])}+1") 
#     return [x for x in str(arr_as_int)] 

# print(increment_array([1,2,3]))