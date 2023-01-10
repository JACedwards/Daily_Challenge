# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

def shortestDist(wordsDict, word1, word2):
    w1_lst = []
    w2_lst = []
    diff_lst = []

    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            w1_lst.append(i)
        elif wordsDict[i] == word2:
            w2_lst.append(i)
    # print(w1_lst, w2_lst)

    for d in w1_lst:
        for e in w2_lst:
            diff_lst.append(abs(d-e))

    return min(diff_lst)




print(shortestDist(["practice", "makes", "perfect", "coding", "makes", "practice", "goober", "gabber", "perfect"], "perfect", "practice"))

#Works if no repeated words
# def shortestDist(wordsDict, word1, word2):
#     w1_index = wordsDict.index(word1)
#     w2_index = wordsDict.index(word2)
#     return w1_index - w2_index




# print(shortestDist(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))