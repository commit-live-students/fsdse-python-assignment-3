def letterAndDigit(str):
    return {
        'DIGITS': sum(c.isdigit() for c in str),
        'LETTERS': sum(c.isalpha() for c in str)
    }
