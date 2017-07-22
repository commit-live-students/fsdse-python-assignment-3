def letterAndDigit(x):
	DIGITS = 0
	LETTERS = 0
	count = {}
	for i in x:
		if i.isalpha():
			LETTERS += 1
		elif i.isdigit():
			DIGITS += 1
	count = {'DIGITS': DIGITS, 'LETTERS' : LETTERS}
	return count
