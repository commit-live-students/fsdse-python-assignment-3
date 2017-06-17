def letterAndDigit(string):
    d={"DIGITS":0, "LETTERS":0}

    for c in string:
        if c.isdigit():
            d["DIGITS"]+=1

        elif c.isalpha():
            d["LETTERS"]+=1
        else:
            pass
    return d
letterAndDigit('geh8745621985')
