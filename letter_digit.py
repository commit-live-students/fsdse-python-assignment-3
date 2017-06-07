def letterAndDigit(userString):
    letter = 0
    digit = 0
    dict = {}
    if userString != None and userString != "":
        print userString
        for i in userString:
            if(i!=" "):
                if i.isalpha():
                    letter = letter + 1
                elif i.isdigit():
                    digit = digit + 1

        dict['DIGITS'] = digit
        dict['LETTERS'] = letter
        print dict
        #return dict['DIGITS']
        #return dict['LETTERS']
        return dict

    else:
        print "Enter a string"

letterAndDigit("dada01! 0001")
