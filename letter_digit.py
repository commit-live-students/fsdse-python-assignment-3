def letterAndDigit(s1):
    dict1 = {"DIGITS":0, "LETTERS":0,'SPACE':0,"OTHER":0}

    numbers = sum(c.isdigit() for c in s1)
    dict1.update({'DIGITS':numbers})

    words   = sum(c.isalpha() for c in s1)
    dict1.update({'LETTERS':words})

    spaces  = sum(c.isspace() for c in s1)
    dict1.update({'SPACE':spaces})

    others  = len(s1) - numbers - words - spaces
    dict1.update({'OTHER':others})

    return dict1
