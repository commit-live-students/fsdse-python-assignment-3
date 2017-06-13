def letterAndDigit(user_str):
    d={}
    count_digits=0
    count_letters=0
    if(user_str!='' and user_str!= None):
        count_letters=sum(i.isalpha() for i in user_str)
        count_digits=sum(i.isdigit() for i in user_str)
        d['DIGITS']=count_digits
        d['LETTERS']=count_letters
    return d
print letterAndDigit("Visa!1 23")
