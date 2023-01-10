# Given an integer array nums, return all consequtive triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

#Psuedo code:
    #slice list into triplets
    #add triplets list
    # loop through and create list containing triplets which
        # sum 0's are present
        # AND without duplicates (using set() and len())
    #remove duplicates

def tripletsZero(nums):
    l = 0
    r = 3
    input_list = []

    while r <= len(nums) - 1:
        slc = nums[l:r]
        input_list.append(slc)
        l +=1
        r += 1
    slc = nums[l:]
    input_list.append(slc)
    # input_list = [[-1, 0, 1], [0, 1, 2], [1, 2, -1], [2, -1, -4]]
    
    zero_only_lst = []
    for trip in input_list:
        if sum(trip) == 0 and len(trip) == len(set(trip)):
            zero_only_lst.append(trip)
   
    return zero_only_lst



print(tripletsZero([-1,0,1,2,-1,-4, 5]))