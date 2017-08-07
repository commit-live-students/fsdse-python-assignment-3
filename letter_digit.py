def letterAndDigit(string):
    if not string:
        return

    string = string.upper()
    LETTERS_PRESET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGITS_PRESET = '1234567890'
    output = {
        'DIGITS': 0,
        'LETTERS': 0,
    }
    for x in string:
        if x in DIGITS_PRESET:
            output['DIGITS'] = output['DIGITS'] + 1
        elif x in LETTERS_PRESET:
            output['LETTERS'] = output['LETTERS'] + 1
        else:
            pass

    return output
