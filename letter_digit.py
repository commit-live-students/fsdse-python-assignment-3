def incdec(d,c):
    try:
        d[c]
        d[c]=d[c]+1
    except KeyError:
        d[c]=1

def letterAndDigit(s):
    d=dict()
    dig=0
    for c in s:
        try:
            int(c)
        except ValueError:
            if(c.isalpha()):
                try:
                    d["LETTERS"]
                    d["LETTERS"]=d["LETTERS"]+1
                except KeyError:
                    d["LETTERS"]=1
        else:
            try:
                d["DIGITS"]
                d["DIGITS"]=d["DIGITS"]+1
            except KeyError:
                d["DIGITS"]=1
    #print d
    return d
        # if(int(c)>int("1") or int(c)<int("9")):
        #     incdec(d,"DIGITS")#d["DIGITS"]=1
        # else:
        #     incdec(d,"LETTERS")#d["LETTERS"]=1
        # try:
        #     d[c]
        #     d[c]=d[c]+1
        # except KeyError:
        #     d[c]=1

letterAndDigit("123asd1")
