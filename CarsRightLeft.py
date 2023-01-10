# In a string we describe a road. There are cars that move to the right and we denote them with ">" and cars that move to the left and we denote them with "<". There are also cameras that are indicated by: ".".
# A camera takes a photo of a car if it moves to the direction of the camera.
# Task
# Your task is to write a function such that, for the input string that represents a road as described, returns the total number of photos that were taken by the cameras. The complexity should be strictly O(N) in order to pass all the tests.

# Examples
# For ">>." - 2 photos were taken
# For ".>>" - 0 photos were taken
# For ">.<." - 3 photos were taken
# For ".><.>>.<<" - 11 photos were taken
#2 + 1 +2+ 3 + 3

#loop through indices in string:
    # check which of three possible characters
        #if > count how many . in slice to right
            # add to counter
        #if < count how many . in slice to left
        #if . continue
    #return count


# def carsRight(s):
#     pic_counter = 0
#     for i in range(len(s)):
#         if s[i] == ">":
#             pic_counter = pic_counter + s[i+1:].count(".")
#         if s[i] == "<":
#             pic_counter = pic_counter + s[:i].count(".")
    
#     return pic_counter

# print(carsRight(".><.>>.<<"))

class Cameras:

    def __init__(self, s):
        self.s = s

    def carsRight(self):
        pic_counter = 0
        for i in range(len(self.s)):
            if self.s[i] == ">":
                pic_counter = pic_counter + self.s[i+1:].count(".")
            if self.s[i] == "<":
                pic_counter = pic_counter + self.s[:i].count(".")
        
        return pic_counter

nicon = Cameras(".><.>>.<<")

print(nicon.carsRight())

