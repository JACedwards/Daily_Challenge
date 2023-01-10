# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

#Psuedo:
#  turn to string
#  Split string
#  sort int versions
#  join as string
#  return int

def digitsDescend(n):

    n = str(n)
    n = list(n)
    n.sort(reverse=True)
    output = ''.join(n)
    return int(output), type(int(output))


print(digitsDescend(42145))