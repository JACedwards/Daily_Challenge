'''Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

# Example 1:
# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
# The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

# Example 2:
# Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# Output: [[1,100],[7,100]]

# Constraints:
# 1 <= items.length <= 1000
# items[i].length == 2
# 1 <= IDi <= 1000
# 0 <= scorei <= 100
# For each IDi, there will be at least five scores'''

#Psuedo code:

    #Identify the two id's through looping and adding to a list
    #store id's in variable, and use it for variable name when creating list of scores for each id
    # loop through items by id, building lists of scores for each of two id's
    # sort 2 sets of scores
    # sum slice of top five scores
    # return list of lists with [id, top-five-average]

def topFiveAve(items):

    ids = []

    for id in items:
        if id[0] not in ids:
            ids.append(id[0])
  
    id_one = ids[0]
    id_two = ids[1]
    scores_one = []
    scores_two = []

    for pairs in items:
        if pairs[0] == id_one:
            scores_one.append(pairs[1])
        elif pairs[0] == id_two:
            scores_two.append(pairs[1])

    scores_one.sort(reverse=True)
    scores_two.sort(reverse=True)

    top_5_one = scores_one[:5]
    top_5_two = scores_two[:5]

    ave_one = sum(top_5_one) // 5
    ave_two = sum(top_5_two) // 5

    output = [[id_one, ave_one], [id_two, ave_two]]
    return output



print(topFiveAve([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))