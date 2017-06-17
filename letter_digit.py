def letterAndDigit(str):
    digits = 0
    letters = 0
    for i in range(len(str)):
        if ord(str[i]) >= 48 and ord(str[i])<=57:
            digits = digits + 1
        elif (ord(str[i])>=97 and ord(str[i])<=122) or (ord(str[i])>=65 and ord(str[i])<=90):
            letters = letters + 1
    return {"DIGITS":digits,"LETTERS":letters}
