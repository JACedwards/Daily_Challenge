# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.
# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

#Pseudo:
    #Count "a's"
        #if not more than 2, 
        #return false
    #Check consecutive L's:
        #use sliding window
        #brute force = slices

#brute force version

# def attendance(record):
#     c_A = record.count('A')
    
#     if c_A > 1:
#         return False

#     c_L = 0
#     for i in range(len(record)):
#         if record[i] == 'L':
#             c_L += 1
#         if c_L == 3:
#             return False
#         if record[i] != 'L':
#             c_L = 0

#     return True

# print(attendance("PPALLL"))


#sliding window  (optimal of three because only one loop, but all three O(n)):

def attendance(record):
    c_A = 0
    c_L = 0

    for i in range(len(record)):
        if record[i] == 'A':
            c_A += 1
        if c_A > 1:
            return False
        if record[i] == 'L':
            c_L += 1
        if c_L == 3:
            return False
        if record[i] != 'L':
            c_L = 0

    return True

print(attendance('PPALLP'))


# more compact double loop
# def attendance(record):

#     return False if 'LLL' in record or record.count('A') > 1 else True
    
# print(attendance('PPALLP'))


