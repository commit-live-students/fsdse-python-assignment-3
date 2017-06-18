def letterAndDigit(line):
    d = l = 0
    for x in line:
        if x.isalpha() == True:
            l = l + 1
        elif x.isdigit() == True:
            d = d + 1
        else:
            pass
    return {"DIGITS":d, "LETTERS":l}
