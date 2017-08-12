s ='world! 234'
def letterAndDigit(s):
    a = dict()
    l=0
    d=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
    a['DIGITS'] = d
    a['LETTERS'] = l
    return a

print letterAndDigit(s)
