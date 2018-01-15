#Displays any Month of the year program

#Initialization
Terminate = 'a'
month_names_eng = ('January', 'February', 'March', 'April', 'May', 'June','July',\
				'August', 'September', 'October', 'November', 'December')
month_names_swe = ('Januari', 'Februari', 'Mars', 'April', 'Maj', 'Juni','Juli',\
				'Augusti', 'September', 'Oktober', 'November', 'December')
month_names_kor = ('1월', '2월', '3월', '4월', '5월', '6월',\
					'7월', '8월', '9월', '10월', '11월', '12월')
month_names_chn = ('一月', '二月', '三月', '四月', '五月', '六月',\
					'七月', '八月', '九月', '十月', '十一月', '十二月')
enddays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

calendar_year = []
month_separator = format(' ', '8')
blank_week = format(' ', '21')
blank_col = format(' ', '3')
end_day_of_week = 7
end_row = 6

while Terminate != 'y':

	##User input
	lang = input('Select language(eng, swe, kor, chn): ')
	lang = lang[0].lower()
	year = int(input('Enter year: '))
	if (year < 1800 or year > 2099):
		year = int(input('Enter year between 1800 ~ 2099: '))
	per_row = int(input('Enter month per row(2~4): '))
	if per_row not in [2, 3, 4]:
		per_row = int(input('Enter month per row between 2~4: '))
		
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
	
	
	##save month_names for selected language
	
	month_names = []
	if lang == 'e':
		month_names = month_names_eng
	elif lang == 's':
		month_names = month_names_swe
	elif lang == 'k':
		month_names = month_names_kor
	elif lang == 'c':
		month_names = month_names_chn
	else:
		month_names = month_names_eng
	
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
	for breaks in range(int(12 / per_row)):
		for month in range(per_row):
			blank_length = 31 - len(month_names[per_row * breaks + month])
			month_name = month_names[per_row * breaks + month] + format(' ', str(blank_length))
			print(month_name, end = '')
		print()
		for week in range(6):
			for month in range(per_row):
				print(calendar_year[per_row * breaks + month][week], month_separator, end = '')
			print()
		print()	
	print()
	
	
	##Re-Initialization
	
	day_of_week = 0
	
	Terminate = input('Press any key to continue(press y for terminate)...')
	
print()