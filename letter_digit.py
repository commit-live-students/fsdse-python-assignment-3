def letterAndDigit(s):
    c=0
    d=0
    if(len(s)>0):
        for i in range(len(s)):
            if(s[i].isalpha()):
               c=c+1
            if(s[i].isdigit()):
               d=d+1
            a={'DIGITS': d , 'LETTERS': c}
        return a
    else:
        return 0
a= letterAndDigit("world! 123")
print a
