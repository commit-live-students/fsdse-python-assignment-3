def letterAndDigit(st):
    alphacount = 0
    numcount = 0
    for i in range(0,len(st)):
        if st[i].isalpha()==True:
            alphacount = alphacount + 1
        if st[i].isdigit()==True:
            numcount = numcount + 1
    return {'DIGITS':numcount,'LETTERS':alphacount}

tmpd=letterAndDigit('123ABC')
print tmpd
