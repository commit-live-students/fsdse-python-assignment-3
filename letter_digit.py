def letterAndDigit(uString):
    letter = 0
    digit = 0
    dict = {}
    if uString != None and uString != "":
        print uString
        for i in uString:
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

letterAndDigit("Greyatom 130617")
