# Given two strings s1 and s2, return True if they are isomorphic, or False if they are not.
# Two strings s1 and s2 are isomorphic if the characters in s1 can be replaced to get s2.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example1:
# In: s1 = "ott", s2 = "add"
# Out: True
# Explained: all o's can be replaced with 'a' and all t's can be replaces with 'd' (o -> a, t -> d)

# Example2:
# In: s1 = "foo", s2 = "bar"
# Out: False
# Explained: f can map to b, but o cannot map to two different letters -- o cannot change to be both a and r


# In: s1 = "paper", s2 = "title"
# Out: True



#psuedo:
# make dictionary of indices for each letter in word for s1 and s2

# see if values equate for each index of dictionary: https://pythonguides.com/python-dictionary-index/




def iso(s1, s2):

    dict1 = {}
    dict2 = {}
    list1 = []
    list2=[]
    x=[]

    for i in range(len(s1)):
        if s1[i] not in dict1:
            dict1[s1[i]] = [i]
        else:
            x = dict1[s1[i]]
            x.append(i)
            dict1[s1[i]] = x

    for i in range(len(s2)):
        if s2[i] not in dict2:
            dict2[s2[i]] = [i]
        else:
            x = dict2[s2[i]]
            x.append(i)
            dict2[s2[i]] = x

    for v in dict1:
        list1.append(dict1[v])

    for v in dict2:
        list2.append(dict2[v])

    return list1 == list2

print(iso("paper", "title"))

