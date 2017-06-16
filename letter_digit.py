def letterAndDigit(tempstr):
    result_dict = {}
    number = 0
    char = 0
    if len(tempstr) > 0:
        for i in range(0,len(tempstr)):
            if (tempstr[i].isdigit()):
                number += 1
            elif (tempstr[i].isalpha()):
                char += 1
            else:
                continue
    result_dict['DIGITS'] = number
    result_dict['LETTERS'] = char
    return result_dict
