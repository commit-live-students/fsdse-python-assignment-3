def letterAndDigit(s1):
    d = {"DIGITS":0, "LETTERS":0}
    for i in s1:
        if i.isalpha():
            d['LETTERS'] +=1
        elif i.isdigit():
            d['DIGITS'] +=1

    return d
