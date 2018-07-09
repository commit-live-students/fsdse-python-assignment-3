def letterAndDigit(string):
    countdict = {'LETTERS':0, 'DIGITS':0}
    for i in string:
        if i in ('!', '.', ' ', '?', ',', ';', ':', "'", '"'):
            string = string.replace(i, "")
    for i in string:
        try:
            i = int(i)
            countdict['DIGITS'] += 1
        except ValueError:
            countdict['LETTERS'] += 1
    return countdict
