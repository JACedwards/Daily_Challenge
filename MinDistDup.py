# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1

#Pseudo code:
        #Count how many times each of word1 and word2 appear in string
        # Dictionary of which word (value) is at each index (key)

    #loop through dictionary k, v:
        #two values == each other:
        #use counter to keep track of smallest distance

def minDistance(word_arr, word1, word2):
    ind_dict = {}
    ind_w1 = []
    ind_w2 = []
    cnt_wrd1 = 0
    cnt_wrd2 = 0
    cnt_min = 0

    cnt_wrd1 = word_arr.count(word1)
    cnt_wrd2 = word_arr.count(word2)
    print(cnt_wrd1, cnt_wrd2)

    for i in range(len(word_arr)):
        ind_dict[i]=word_arr[i]
    print(ind_dict)
    #ind_dict = {0: 'practice', 1: 'makes', 2: 'perfect', 3: 'coding', 4: 'makes'}


    for k, v in ind_dict.items():
        if v == word1:
            ind_w1.append(k)
        if v == word2:
            ind_w2.append(k)
    print(ind_w1, ind_w2)

    for one in ind_w1:
        for two in ind_w2:
            diff = one - two
            if cnt_min == 0:
                cnt_min = abs(diff)
            elif cnt_min > abs(diff):
                cnt_min = abs(diff)
    return cnt_min

print(minDistance(["practice", "makes", "perfect", "coding", "makes", "goober", "goober", "goober", "coding"], "makes", "coding"))


