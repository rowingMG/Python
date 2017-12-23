#Gives days of entered month

#Grettings
print('This program will display the number of days in a given month.')
valid_input = True

#User input
year = int(input('Enter the year: '))
month = int(input('Enter the month: '))

#determine the days

#February
if month == 2:
	if (year % 4 == 0 and not(year % 100 == 0) and year % 400 == 0):
		num_days = 29
	else:
		num_days = 28
		
#else
elif month in (1, 3, 5, 7, 8, 10, 12):
	num_days = 31
elif month in (4, 6, 9, 11):
	num_days = 30
else:
	print('Invalid input.')
	valid_input = False

if valid_input:
	print('\nThere are', num_days, 'in the given month.')