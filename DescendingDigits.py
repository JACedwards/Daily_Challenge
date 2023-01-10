# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

#Psuedo:
#change int to string
#split string into list
#sort reverse=True
#change back to int

def descendingDigits(n):

    n = str(n)
    lst = list(n)
    lst.sort(reverse=True)
    output = ''.join(lst)
    return int(output)



print(descendingDigits(145263))


