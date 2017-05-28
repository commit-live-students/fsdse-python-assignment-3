string = 'rupalihangkar123'
d={}

def letterAndDigit(string):
    count_aplha = 0
    count_num = 0
    count_num = sum(i.isdigit() for i in string)
    count_aplha = sum(j.isalpha() for j in string)
    d["DIGITS"] = count_num
    d["LETTERS"] = count_aplha

    return d

if len(string) > 0:
    a = letterAndDigit(string)
    print a
