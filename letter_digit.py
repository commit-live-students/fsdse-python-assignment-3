def letterAndDigit(String):
    letter = 0
    digit = 0
    dict = {}
    if String != None and String != "":
        print String
        for i in String:
            if(i!=" "):
                if i.isalpha():
                    letter = letter + 1
                elif i.isdigit():
                    digit = digit + 1

        dict['DIGITS'] = digit
        dict['LETTERS'] = letter
        print dict

        return dict

    else:
        print "Enter a string"

letterAndDigit("pankaj02! 0002")
