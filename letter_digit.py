def letterAndDigit(string1):
    ch=dg=0
    for c in string1:
        if c.isalpha() == True:
            ch += 1
        elif c.isdigit() == True:
            dg += 1
        else:
            pass
    return({"LETTERS":ch, "DIGITS":dg})
print letterAndDigit('world! 234')
