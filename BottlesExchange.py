# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
# Input: numBottles = 9, numExchange = 3
# Output: 13
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
# ----------------------------------------------------------------------------------
# Input: numBottles = 15, numExchange = 4
# Output: 19
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
# Number of water bottles you can drink: 15 + 3 + 1 = 19.

#Pseudo code:
    #count = numBottles
    # floor divide numBottles by numExchange
    # divide numBottles by result of previous
        #add result of previous....

#  15 + 3 + 1 = 19
# def bottleEX(numBottles, numExchange):
#     count = numBottles
#     #15
#     full_for_empty = numBottles // numExchange
#     print(f'Fex_ful = {full_for_empty}')
#     count = count + full_for_empty
#     #18
#     full_for_empty_2 = (full_for_empty + (numBottles % numExchange)) // numExchange
#     print(f'full_for_empty_2 == {full_for_empty_2}')
    
#     count = count + full_for_empty_2
#     return count

# print(bottleEX(15, 4))

#Recursion:

#15 + 3 + 1 = 19

def bottleEx(numBottles, numExchange):
    count = numBottles
    mod = 0
 
    while numBottles >= numExchange:
        mod = numBottles % numExchange
        full_for_empty = numBottles // numExchange
        count = count + full_for_empty
        numBottles = mod + full_for_empty
        
    return count

print(bottleEx(9, 3))
print(bottleEx(15,4))
