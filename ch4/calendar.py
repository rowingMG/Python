#Displays any Month of the year program

#Initialization
Terminate = 'a'
month_names = ('January', 'Feburary', 'March', 'April', 'May', 'June','July',\
				'August', 'September', 'October', 'November', 'December')
enddays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

calendar_year = []
month_separator = format(' ', '8')
blank_week = format(' ', '21')
blank_col = format(' ', '3')
end_day_of_week = 7
end_row = 6

while Terminate != 'y':

	##User input
	
	year = int(input('Enter year: '))
	if (year < 1800 or year > 2099):
		year = int(input('Enter year between 1800 ~ 2099: '))

		
	##Calculate leap year and give values to Feburary
	
	if year % 4 == 0 and not(year % 100 == 0) and year % 400 == 0:
		leapyear = True
		enddays[1] = 29
	else:
		leapyear = False
		enddays[1] = 28

		
	##Day of week Calculation
	
	#calculate day of the week of day 1, January
	century_digits = year // 100

	year_digits = year % 100

	key_value = year_digits + year_digits // 4

	if century_digits == 18:
		key_value = key_value + 2
	elif century_digits == 20:
		key_value = key_value + 6
		
	if not leapyear:
		key_value = key_value + 1
		
	#Determine start day of Jan 1
	key_value = (key_value + 1) % 7
	if key_value == 0:
		day_of_week = 7
	else:
		day_of_week = key_value
		
	day_of_week = day_of_week - 1
	
	
	##save days into lists
	
	for month in range(12):
		
		calendar_month = []
		current_day = 1
		
		#For first week
		calendar_week = ''
		current_col = 0
		current_row = 0
		#Fill the blanks for the first week
		while current_col < day_of_week:
			calendar_week = calendar_week + blank_col
			current_col = current_col + 1
		while day_of_week < end_day_of_week:
			calendar_week = calendar_week + format(str(current_day), '>3')
			current_day = current_day + 1
			day_of_week = day_of_week + 1
		calendar_month = calendar_month + [calendar_week]
		day_of_week = day_of_week % 7
		
		#Weeks 2~5
		calendar_week = ''
		current_row = 1
		while current_row < end_row - 1:
			while day_of_week < end_day_of_week and current_day <= enddays[month]:
				calendar_week = calendar_week + format(str(current_day), '>3')
				current_day = current_day + 1
				day_of_week = day_of_week + 1
			
			#Fill the blanks for the Week 5
			if current_row == 4:
				current_col = day_of_week
				while current_col < end_day_of_week:
					calendar_week = calendar_week + blank_col
					current_col = current_col + 1
			calendar_month = calendar_month + [calendar_week]
			day_of_week = day_of_week % 7
			calendar_week = ''
			current_row = current_row + 1
			
		day_of_week = day_of_week % 7
		
		#Week 6
		calendar_week = ''
		#In case of Week 6 is blank week
		if current_day > enddays[month]:
			calendar_week = blank_week
		#In case of Week 6 is not a blank week
		else:
			while current_day <= enddays[month]:
				calendar_week = calendar_week + format(str(current_day), '>3')
				current_day = current_day + 1
				day_of_week = day_of_week + 1
			current_col = day_of_week
			while current_col < end_day_of_week:
				calendar_week = calendar_week + blank_col
				current_col = current_col + 1
		calendar_month = calendar_month + [calendar_week]
		day_of_week = day_of_week % 7
		
		#add the whole month to the year
		calendar_year = calendar_year + [calendar_month]
	
	
	##Print the Results
	
	#print year first
	print()
	print(year, '\n')
	
	#print others
	for quarter in range(4):
		for month in range(3):
			blank_length = 31 - len(month_names[3 * quarter + month])
			month_name = month_names[3 * quarter + month] + format(' ', str(blank_length))
			print(month_name, end = '')
		print()
		for week in range(6):
			for month in range(3):
				print(calendar_year[3 * quarter + month][week], month_separator, end = '')
			print()
		print()	
	print()
	
	
	##Re-Initialization
	
	day_of_week = 0
	
	Terminate = input('Press any key to continue(press y for terminate)...')
	
print()