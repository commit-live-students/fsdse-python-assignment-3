def letterAndDigit(str):
	Digit = 0
	character = 0
	y = {}
	for i in str:
		if i.isalpha():
			character +=1
		elif i.isdigit():
			Digit +=1
		y.update({'DIGITS': Digit})
                y.update({'LETTERS': character})

	return y

print letterAndDigit('536yuworld! 234')
