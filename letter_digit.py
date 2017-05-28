def letterAndDigit(s):
    import re
    if s is None or "":
        print("string should not be empty or None")
        return 1
    all_numbers = ''.join(re.findall('[0-9]+', s))
    all_letters = ''.join(re.findall('[a-zA-z]+', s))
    return {'DIGITS': len(all_numbers), 'LETTERS': len(all_letters)}
