def letterAndDigit(n):
    numbers = sum(c.isdigit() for c in n)
    letters = sum(c.isalpha() for c in n)
    return {'DIGITS':numbers, 'LETTERS':letters  }
