# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

#Loop through ransomNote, 
#check if each letter in magazine
    #if in magazine:
        #remove that single occurance
#     else:  return False
# return True

def ransomSpell(ransomNote, magazine):

    for lt in ransomNote:
        if lt in magazine:
            magazine=magazine.replace(lt, "", 1)
        else:
            return False
    return True


print(ransomSpell("baad", "badz7se"))

# from collections import Counter
# def ransomNote(note, mag):
#     print(Counter(note), Counter(mag))  
#     return Counter(note) <= Counter(mag)

# print(ransomNote("baad", "baadz7se"))

