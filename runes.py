# You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.
# The archaeologist will give you a simple math expression, of the form
# [number][op][number]=[number]
# He has converted all of the runes he knows into digits.
# The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear.
# Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
# If there are ?s in an expression, they represent a digit rune that the archaeologist doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
# Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the archaeologist - it means that he's got some of his runes wrong. output -1 in that case.
# 
# Examples:
# 
# Input: "1+1=?"
# Output: 2
# -----------------
# 
# Input: "??*??=302?"
# Output: 5
# -----------------
# 
# Input: "??*1=??"
# Output: 2

#Pseudo code:
    # break string into four parts, ignoring equal sign.
        #first num = a
        #operand = op_char
        #second num = b
        #sum/product = output

#This should work for negative integers and if the operand is + or *.
#Haven't yet made it work if operand is "-"

import operator

def runes(string):
    test = ['0','1','2','3','4','5','6','7','8','9', "?", "-"]
    lst_o_strings = []
    ind_strings = ''

    for i in range(len(string)):
        if string[i] in test:
            ind_strings = f"{ind_strings}{string[i]}"
        else:
            lst_o_strings.append(ind_strings)
            lst_o_strings.append(string[i])
            ind_strings = ''
    lst_o_strings.append(ind_strings)
    
    a_s = lst_o_strings[0]     
    op_char = lst_o_strings[1] 
    b_s = lst_o_strings[2]     
    output_s = lst_o_strings[4] 

    digits = ['1','2','3','4','5','6','7','8','9']
    digit_list = []

    for d in string:
        if d in digits:
            digit_list.append(int(d))
    digit_set = set(digit_list)

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }  

    numerals = [1,2,3,4,5,6,7,8,9]
    for q in numerals:
        if q not in digit_set:
            ind_str_a = ''

            for s in a_s:
                if s == '?':
                    ind_str_a = f'{ind_str_a}{q}'
                else:
                    ind_str_a = f'{ind_str_a}{s}'
            
            ind_str_b = ''

            for s in b_s:
                if s == '?':
                    ind_str_b = f'{ind_str_b}{q}'
                else:
                    ind_str_b = f'{ind_str_b}{s}'
            
            ind_str_output = ''

            for s in output_s:
                if s == '?':
                    ind_str_output = f'{ind_str_output}{q}'
                else:
                    ind_str_output = f'{ind_str_output}{s}'
            
            a = int(ind_str_a)
            b = int(ind_str_b)
            output = int(ind_str_output)
            result = ops[op_char](a,b)
            if result == output:
                return q
            else:
                ind_str_a = ''
                ind_str_b = ''
                ind_str_output = ''
                
    return -1

print(runes("-??*??=-302?"))



##Once have original separated into these strings:
    #num-a
    #operand
    #num-b
    #num-c (output)
#should be able to use rest of this to finish up

# import operator

# ops = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }   



# q = 5


# a = int(f'{q}{q}')
# b = int(f'{q}{q}') 
# op_char = '*'

# result = ops[op_char](a,b)
# if result == int(f'302{q}'):
#     print(True)
