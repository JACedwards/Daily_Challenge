# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
# Example 1:
# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
# The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
# # Example 2:
# # Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# Output: [[1,100],[7,100]]

#Psuedo:
# list of zero indices of each list in array
# for indices of list of zero indices:
    #loop through each item in input list
    #if index 0 of list in input == current index of list of indices
        # append index 1 to list of scores...

def studAveScores(arr):
    key_list = []
    d_id_lsc = {}
    intr_list=[]
    
    for itm in arr:
        key_list.append(itm[0])
    ky_list_set =set(key_list)
    key_list = list(ky_list_set)

    for n in key_list:
        for lt in arr:
            if lt[0] == n:
                intr_list.append(lt[1])
                d_id_lsc[n]=intr_list
        intr_list = []

    #{1: [91, 92, 60, 65, 87, 100], 2: [93, 97, 77, 100, 76]}

    for k, v in d_id_lsc.items():
        v.sort(reverse=True)
        v=v[0:5]
        d_id_lsc[k]=v

    sum = 0
    ave = 0

    {1: [100, 92, 91, 87, 65], 2: [100, 97, 93, 77, 76]}

    for k, v in d_id_lsc.items():
        for n in v:
            sum = sum + n
        ave = sum // 5
        d_id_lsc[k] = ave
        sum=0
        ave=0

    output = list(d_id_lsc.items())
    
    final = []
    for itm in output:
        x = list(itm)
        final.append(x)
    
    return final

        
print(studAveScores([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))

# Output: [[1,87],[2,88]]



#*****hard coded version****


# def studAveScores(arr):
#     s_id1 = []
#     s_id2 = []
#     top_fv1 = []
#     top_fv2 = []
#     output1 = []
#     output2 = []
    
#     for id in arr:
#         if id[0] == 1:
#             s_id1.append(id[1])
#         else:
#             s_id2.append(id[1])
    
#     #scores sorted in descending order
#     s_id1.sort(reverse=True)
#     s_id2.sort(reverse=True)

#     #slice top 5 scores
#     top_fv1 = s_id1[0:5]
#     top_fv2 = s_id2[0:5]

#     tp_ave1 = 0
#     tp_ave2 = 0

#     for n in top_fv1:
#         tp_ave1 = tp_ave1 + n
#     tp_ave1 = tp_ave1 // 5

#     for n in top_fv2:
#         tp_ave2 = tp_ave2 + n
#     tp_ave2 = tp_ave2 // 5

#     output1 = [1]
#     output2 = [2]

#     output1.append(tp_ave1)
#     output2.append(tp_ave2)

#     final = []
#     final.append(output1)
#     final.append(output2)

#     return final

# print(studAveScores([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))

# Output: [[1,87],[2,88]]







    #keylist = [1,2]
    #arr=[[1,91],[2,93],[1,60]]
    #round 1:
        # n = 1
        # lt = [1,91]
        #lt[0] = 1
        # intr_list.append(lt[1]) =[91]
        # d_id_slc[n]=intr_list = {1:[91]}

    #round 2:
        # n = 1
        # lt = [2,93]
        #lt[0] = 2
        # d_id_slc[n]=intr_list = {1:[91]}

    #round 3:
        # n = 1
        # lt = [1,60]
        #lt[0] = 1
        # intr_list.append(lt[1]) =[91,60]
        # d_id_slc[n]=intr_list = {1:[91,60]}




