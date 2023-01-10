# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ithathlete.
# Example 1:
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
# Constraints:
# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106

# Psuedo code:
    #sort array, descending
    #create dictionary
    #--assigning place labels to each number in sorted array
    #create list of labels in original indexed order

def rankAth(arr):
    
    orgn_order = arr
    orgn_order = tuple((orgn_order))
    arr.sort(reverse=True)

    dict_labels = {}

    dict_labels[arr[0]] = "Gold Medal"
    dict_labels[arr[1]] = "Silver Medal"
    dict_labels[arr[2]] = "Bronze Medal"
   
    non_medal = arr[3:]
    n=4
    
    for i in range(len(non_medal)):
        dict_labels[non_medal[i]] = n
        n+=1

    output = []
    
    for rank in orgn_order:
        output.append(dict_labels.get(rank))

    return output

print(rankAth([10,3,8,9,4]))

