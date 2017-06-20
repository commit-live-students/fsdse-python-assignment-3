def letterAndDigit(str):

    if ( str != "") :

        count_Digits = 0
        count_Letters = 0

        for i in str :
            if i.isdigit() :
                count_Digits = count_Digits + 1
            if i.isalpha() :
                count_Letters = count_Letters + 1
            else :
                pass

        dict = {"DIGITS":count_Digits, "LETTERS":count_Letters}
        return dict

letterAndDigit('world! 234')
