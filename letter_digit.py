def letterAndDigit(s):

    l1=list(''.join(s))
    letters=digits=something=0
    if len(l1)==0:
        print "The String is Empty"
    else:
        for i in l1 :
            if i.isalpha():
                letters+=1
            elif i.isdigit():
                digits+=1
            else:
                something+=1
    d={}
    d['DIGITS']=int(digits)
    d['LETTERS']=letters
    return d
letterAndDigit("Hello World! 123")
