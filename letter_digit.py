def letterAndDigit (strIn):
    if not strIn:
        print "Pass non-empty string"
        return {}
    else:
        length = len(strIn)
        digit = 0
        letters = 0
        space = 0
        other = 0
        for ch in strIn:
            if ch.isalpha():
                letters += 1
            elif ch.isdigit():
                digit += 1
            elif ch.isspace():
                space += 1
            else:
                other += 1
        return {"DIGITS":digit, "LETTERS":letters}

if __name__ == "__main__":
    print letterAndDigit ("")
    print letterAndDigit ("   ")
    print letterAndDigit ("a24terte5y   =df")
