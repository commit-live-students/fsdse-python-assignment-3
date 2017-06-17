
def letterAndDigit(s):
     d=l=0
     for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
     d1={"DIGITS": d, "LETTERS": l}

     return d1
     print d1
print letterAndDigit("abcd123")
