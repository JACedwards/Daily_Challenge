# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true

# Pseudo code:
#   Loop through indices of arr:
#       if arr[i][0] < arr[i+1[0] and arr[i][1] > arr[i+1][0]:
            # return False
#             

def meetAttend(arr):

    for i in range(len(arr)-1):
        if arr[i][0] < arr[i+1][0] and arr[i][1] > arr[i+1][0]:
            return False
        # elif [i][0] < arr[i+1][0] and arr[i][1] < arr[i+1][0]:
        #     continue
        elif [i][0] > arr[i+1][0]:
            if arr[i+1][1] > arr[i][0]:
                return False 

    return True



print(meetAttend([[5,10],[15,20], [0,30]]))