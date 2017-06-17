def letterAndDigit(string):
    d = {"DIGITS": 0, "LETTERS": 0}
    for char in string:
        if char.isdigit():
            d["DIGITS"] += 1
        elif char.isalpha():
            d["LETTERS"] += 1
    return d

string = "Saahil 1920"
letterAndDigit(string)
