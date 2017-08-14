def letterAndDigit(n):
    d = {}
    digits = sum(c.isdigit() for c in n)
    letters = sum(c.isalpha() for c in n)
    d['DIGITS'] = digits
    d['LETTERS'] = letters
    return d

'''
print letterAndDigit(raw_input('Enter string : '))
'''
