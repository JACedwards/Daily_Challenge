# Given a string of space separated integers
# Return the highest and lowest as a space separated string "-5 83"
# bonus challenge: do so for strings of numbers with random extra whitespace
# Example:
# Input: "32 27 83 25 5 -5 0 32"
# Output: "-5 83"

# Bonus Example:
# Input: "     82  1 0  -5 32  7  14  22   "
# Output: "-5 82"

#Psuedo code:
    #split into list
    # find max int()
    # find min int()
    # return as string with space


# def highestLowest(arr):
    
#     lst = arr.split()
#     h = max(lst)
#     l = min(lst)
#     output = f"{l} {h}"

#     return output

def highestLowest(arr):


    l = 0
    x = int(arr[0:2])

    print(x, type(x))
    if x > l:
        print('greater')
    else:
        print('lesser')
    # print(x, print(type(arr[0:2])))
    # print(hi, type(hi))



print(highestLowest("32 27 83 25 5 -5 0 32"))
    