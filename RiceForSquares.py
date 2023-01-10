
#October 19
# 
# # There is a simple constant time answer for this problem- but I want you all to solve it using recursion! (bonus points if you also figure out the constant time answer) Also, this is a codewars problem so you may have seen it before. Problem below:

# I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 4 for the third, 8 for the fourth and so on, always doubling the previous.

# Your task is pretty straightforward (but not necessarily easy): given an amount of grains, you need to return up to which square of the chessboard one should count in order to get at least as many.

# As usual, a few examples might be way better than thousands of words from me:

# squares_needed(0) == 0
# squares_needed(1) == 1
# squares_needed(2) == 2
# squares_needed(3) == 2
# squares_needed(4) == 3

# Input is always going to be valid/reasonable: ie: a non negative number; extra cookie for not using a loop to compute square-by-square (at least not directly) and instead trying a smarter approach [hint: some peculiar operator]; a trick converting the number might also work: impress me!

#Pseudo:
    # if 0 = 0    
    # if 1 = 1
    # if 2 = 2

    #create list of all possible square/grain values using range up to number of grans input
    #loop through list with a grain counter (while)
    # return number of squares when reach grain count



class RiceSquares():

    def __init__(self, gns):
        self.gns = gns
    
    def grainsAndSquares(self):

        # for g in range(3, gns+1):
        #     print(g)
        if self.gns == 0:
            return 0
        if self.gns == 1:
            return 1
        if self.gns == 2:
            return 2
            
        count_grains = 2
        count_squares = 3
        lst_sq_values = []
        dct_sq_gr = {}

        while count_grains <= self.gns:
            count_grains = count_grains * 2
            lst_sq_values.append(count_grains)
            dct_sq_gr[count_squares] = count_grains
            count_squares += 1

        rev_dct_sq_gr = {}
        for k, v in reversed(dct_sq_gr.items()):
            rev_dct_sq_gr[k] = v

        for k, v in rev_dct_sq_gr.items():
            if self.gns >= v:
                return k

rice17 = RiceSquares(33)
print(rice17.grainsAndSquares())



#*****working function version
# def grainsAndSquares(gns):

#     # for g in range(3, gns+1):
#     #     print(g)
#     if gns == 0:
#         return 0
#     if gns == 1:
#         return 1
#     if gns == 2:
#         return 2
        
#     count_grains = 2
#     count_squares = 3
#     lst_sq_values = []
#     dct_sq_gr = {}

#     while count_grains <= gns:
#         count_grains = count_grains * 2
#         lst_sq_values.append(count_grains)
#         dct_sq_gr[count_squares] = count_grains
#         count_squares += 1

#     rev_dct_sq_gr = {}
#     for k, v in reversed(dct_sq_gr.items()):
#         rev_dct_sq_gr[k] = v

#     print(rev_dct_sq_gr)

#     for k, v in rev_dct_sq_gr.items():
#         if gns >= v:
#             return k

# print(grainsAndSquares(33))