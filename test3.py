def get_matrix(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    else:
        output_lst = []
        output = []
        count = 0
        zero_matrix = []
        lst_zero = [0]*n
        zero_matrix = [lst_zero]*n
        print(zero_matrix)

        for l in zero_matrix:  
            l[count] = 1
            output.append(l)
            count +=1
        return output

print(get_matrix(2))    