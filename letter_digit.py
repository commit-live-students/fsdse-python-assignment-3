def letterAndDigit(inputString):
    countOfdigit = 0
    countOfChar  = 0

    d = dict()

    if(len(inputString) == 0):
        print 'string should not be empty'

    for x in (inputString):


        if x.isalpha():
            countOfChar = countOfChar + 1
        if x.isdigit():
            countOfdigit = countOfdigit + 1


    d["DIGITS"] = countOfdigit
    d["LETTERS"] = countOfChar

    return d

print letterAndDigit("abs&&123ghte1")
