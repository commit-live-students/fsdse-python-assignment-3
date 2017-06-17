def letterAndDigit(x):
    letters = digits = other = 0
    for i in x:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
    return {"DIGITS" : digits , "LETTERS" : letters}

#print letterAndDigit("Python 3.2")
