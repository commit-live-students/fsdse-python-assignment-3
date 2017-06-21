# Calculate the number of letters and digits\pair_len = int(raw_input("Len of pair: "))
str_eg = 'world234'

def letterAndDigit(stri):
    str_eg2 = list(stri)
    dig = 0
    letter = 0
    for e in str_eg2:
        if (e.isdigit() == True):
            dig = dig + 1
        elif (e.isalpha() == True):
            letter = letter + 1
        else:
            continue
    x = [dig, letter]
    ans = {}
    ans["DIGITS"] = dig
    ans["LETTERS"] = letter
    print (ans)
    return ans

letterAndDigit(str_eg)
