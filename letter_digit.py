
def letterAndDigit(input_string):
    letters_count, digits_count = 0, 0
    if input_string is None or len(input_string) == 0:
        return
    chars = map(None, input_string)
    print chars
    for char in chars:
        if ord(char) in range(48, 58):
            digits_count += 1
        elif ord(char) in range(65,91) or ord(char) in range(97, 123):
            letters_count += 1
    return {"DIGITS": digits_count, "LETTERS": letters_count}
