def letterAndDigit(s):
    numbers = sum(c.isdigit() for c in s)
    letters   = sum(c.isalpha() for c in s)
    dict = {"DIGITS":numbers,"LETTERS":letters}
    return dict



print letterAndDigit("i 4 sanket bhat2 123")
