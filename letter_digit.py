def letterAndDigit(string):
    count1=0
    count2=0
    for character in string:
        if character.isdigit():
            count1 += 1
        elif character.isalpha():
            count2 += 1
        elif character == " ":
            pass

    return {"DIGITS": count1 ,"LETTERS": count2}
