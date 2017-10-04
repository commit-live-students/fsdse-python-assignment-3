strng = 'world! 234' # string argument
def letterAndDigit(str1):
    assert isinstance(str1,str),'input variable should be a string'
    diglist = []
    alplist = []
    for c in list(str1):
        if c.isdigit():
            diglist.append(c)
        elif c.isalpha():
            alplist.append(c)
    countdig = len(diglist)
    countchr = len(alplist)
    return {'DIGITS':countdig, 'LETTERS':countchr}

letterAndDigit(strng)
