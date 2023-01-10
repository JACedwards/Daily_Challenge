def numTransformations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    az = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    x = words[0][0].upper()
    y = az.index(x)
    z = morse[y]
    concat=''
    output=[]
    

    for w in words:
        for i in range(len(w)):
            # print(words[i])
            alpha_in = az.index(w[i].upper())
            mrs = morse[alpha_in]
            # print(mrs)
            concat = concat + mrs
        # print(concat)
        output.append(concat)
        # print(output)
        concat=''
    
    # print(output)

    ind=0
    count=1
    
    while ind+1 <= len(words) - 1:
        if output[ind] != output[ind + 1]:
            count+=1
            ind+=1
        else:
            ind+=1

    return count

print(numTransformations(["gin","zen","gig","msg"]))

    # for w in words:
    #     for i in range(len(w)):
    #         print(w[i])
    #         code = az.index(w[i].upper())
    #         print(code)
    #         trans_code = morse[code]
    #         print(trans_code)
    #         concat = concat + trans_code
    #         print(concat)

    #         break