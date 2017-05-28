def letterAndDigit(str1='default123'):
    cntLetter = 0
    cntDigit = 0
    for s in str1:
        if str.isdigit(s) == True:
            cntDigit+=1
        if str.isalpha(s) == True:
            cntLetter+=1

    cntDict = {}
    cntDict.update({"DIGITS":cntDigit, "LETTERS":cntLetter})
    return cntDict

print(letterAndDigit('Nikhil123'))
