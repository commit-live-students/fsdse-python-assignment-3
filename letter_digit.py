dic = {'DIGITS':'', 'LETTERS':''}
a = 0
b = 0
def letterAndDigit(a):
	b =len(a)
	alpha = 0
	num = 0
	for i in range(0,b):
		if(a[i].isalpha()):
			alpha +=1

		elif(a[i].isdigit()):
			num +=1
	dic['DIGITS'] = num
	dic['LETTERS'] = alpha
	return dic

string = "world! 234"
letterAndDigit(string)
