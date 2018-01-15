def displayWelcome():

	print('This program will convert a range of tempertures.')
	print('Enter two temperature metric, F for Fahrenheit, C for Celsius, K for Kelvin')
	print('For example, enter FC to convert Fahrenheit to Celsius.\n')
	
def getConvertTo():
	valid_input = ('FC', 'CF', 'FK', 'KF', 'CK', 'KC')
	which = input('Enter selection: ')
	while which not in valid_input:
		which = which = input('Enter correct selection: ')
	
	return which
	
def tempConversion(which, origin):
	if which == 'FC':
		change = (origin - 32) * 5/9
	elif which == 'CF':
		change = (9/5 * origin) + 32
	elif which == 'FK':
		change = (origin - 32) * 5/9 + 273.15
	elif which == 'KF':
		change = (9/5 * (origin + 273.15)) + 32
	elif which == 'CK':
		change = origin + 273.15
	elif which == 'KC':
		change = origin - 273.15
	else:
		print('incorrect selection!')
		return
	
	return change
	
def displayConversion(which, start, end):
	metric_names = (('F', 'Fahrenheit'), ('C', 'Celsius'), ('K', 'Kelvin'))
	
	for k in metric_names:
		if which[0] == k[0]:
			original_name = k[1]
		elif which[1] == k[0]:
			change_name = k[1]
			
	print('\n   Degrees', ' Degrees')
	print(original_name, change_name)
	
	for temp in range(start, end + 1):
		converted_temp = tempConversion(which, temp)
		print('  ', format(temp, '4.1f'), '   ', format(converted_temp, '4.1f'))
		
##-----Main-----##

#Display program welcome
displayWelcome()

#Get which convertion from user
which = getConvertTo()

#Get range of tempertures to convert
temp_start = int(input('Enter starting temperature to convert: '))
temp_end = int(input('Enter ending temperature to convert: '))

#Display range of converted temperatures
displayConversion(which, temp_start, temp_end)