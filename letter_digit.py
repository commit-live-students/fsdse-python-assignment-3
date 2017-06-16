def letterAndDigit(s):
    if(s==""or s==None):
        return None
    w=0
    d=0
    for i in range(len(s)):
        if(s[i].isalpha()):
            w=w+1
        if(s[i].isdigit()):
            d=d+1
    return {"DIGITS": d, "LETTERS": w}
ans = letterAndDigit('world! 234')
print(ans)
