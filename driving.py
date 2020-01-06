country = input('Input country: ')
age = input('Input age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive')
	else:
		print('You cannot drive')
