def letterAndDigit(user_string):
    d = {}
    total_words = 0
    total_digits = 0
    if user_string != None or user_string != "":
        total_digits = sum(i.isdigit() for i in user_string)
        total_words = sum(i.isalpha() for i in user_string)
        d['DIGITS'] = total_digits
        d['LETTERS'] = total_words
    return d
