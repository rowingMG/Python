#Displays any Month of the year program

Terminate = 'a'

while Terminate != 'y':
#User input
	year = int(input('Enter year: '))
	if (year < 1800 or year > 2099):
		year = int(input('Enter year between 1800 ~ 2099: '))
	month = int(input('Enter month: '))
	if (month < 1 or month > 12):
		month = int(input('Enter valid month between 1 ~ 12: '))

#Calculate leap year
	if year % 4 == 0 and (not(year % 100 == 0) and year % 400 == 0):
		leapyear = True
	else:
		leapyear = False

#Calculate End of the month
	if month == 2:
		if leapyear:
			lastday = 29
		else:
			lastday = 28
			
	elif month in (1, 3, 5, 7, 8, 10, 12):
		lastday = 31
		
	else:
		lastday = 30

#calculate day of the week of day 1
	century_digits = year // 100

	year_digits = year % 100

	key_value = year_digits + year_digits // 4

	if century_digits == 18:
		key_value = key_value + 2
	elif century_digits == 20:
		key_value = key_value + 6
		
	if month == 1 and not leapyear:
		key_value = key_value + 1
	elif month == 2:
		if leapyear:
			key_value = key_value + 3
		else:
			key_value = key_value + 4
	elif month == 3 or month == 11:
		key_value = key_value + 4
	elif month == 5:
		key_value = key_value + 2
	elif month == 6:
		key_value = key_value + 5
	elif month == 8:
		key_value = key_value + 3
	elif month == 10:
		key_value = key_value + 1
	elif month == 9 or month == 12:
		key_value = key_value + 6

	key_value = (key_value + 1) % 7
	if key_value == 0:
		key_value = 7
	key_value = key_value - 1

#Display month and year, day of the week

#Determine month
	if month == 1:
		month_name = 'JANUARY'
	if month == 2:
		month_name = 'FEBRURARY'
	if month == 3:
		month_name = 'MARCH'
	if month == 4:
		month_name = 'APRIL'
	if month == 5:
		month_name = 'MAY'
	if month == 6:
		month_name = 'JUNE'
	if month == 7:
		month_name = 'JULY'
	if month == 8:
		month_name = 'AUGUST'
	if month == 9:
		month_name = 'SEPTEMBER'
	if month == 10:
		month_name = 'OCTOBER'
	if month == 11:
		month_name = 'NOVEMVER'
	if month == 12:
		month_name = 'DECEMBER'
		
#Then print
	print('\n', '  ' + month_name, year)

#day of the week
	print('{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}'.format('Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat'))

#print days
	temp_key = key_value
	temp_lastday = lastday
	days = 1
	while temp_key != 0:
		print('      ', end = '')
		temp_key = temp_key - 1
	while temp_lastday >= days:
		if key_value == 6:
			print('{:6}'.format(days))
		else:
			print('{:6}'.format(days), end = '')
		days = days + 1
		key_value = (key_value + 1) % 7
		
	print()
	
	Terminate = input('Press any key to continue(press y for terminate)...')
	
print()
	
	