# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

#Pseudo:
#solve first for always starting at index 0
#store number of last index
#while loop, ind <= last index
#sum1 = 0 (for storing how much spent)
#ind = 0 (or 1 if decide to start at 1)
#add value for index 0 to sum1
#check to see if ind+1 value or ind+2 value is greater
#take lesser and add that vaule to running index

# Input: cost = [10,15,20]
def costOfSteps(cost):

    top_ind = len(cost)-1
    #2
    sum1 = 0
    sum2 = 0
    
    ind = 0
    one_step = 0
    two_step = 0
    while ind <= top_ind-1:
        sum1 = sum1 + cost[ind]
        #10
        one_step = cost[ind+1]
        try:
            two_step = cost[ind+2]
        except:
            two_step = cost[ind+1]

        if one_step <= two_step:
            ind=ind+1
        else:
            ind=ind+2

    ind = 1
    one_step = 0
    two_step = 0
    while ind <= top_ind-1:
        sum2 = sum2 + cost[ind]
        #10
        one_step = cost[ind+1]
        try:
            two_step = cost[ind+2]
        except:
            two_step = cost[ind+1]

        if one_step <= two_step:
            ind=ind+1
        else:
            ind=ind+2
    
    if sum1<sum2:
        return sum1
    return sum2



print(costOfSteps([1,100,1,1,1,100,1,1,100,1]))

