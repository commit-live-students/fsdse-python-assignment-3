def letterAndDigit(s):
    dictionary = dict()
    count_of_letters = 0
    count_of_digits = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            count_of_letters += 1
        elif s[i] >= '0' and s[i] <= '9':
            count_of_digits += 1
    dictionary['DIGITS'] = count_of_digits
    dictionary['LETTERS'] = count_of_letters
    return dictionary

s = 'world! 234'
print letterAndDigit(s)
