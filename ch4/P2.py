##4-P2: Save only number in tuple - 'valid_values'

#Initialization
Terminate = False
valid_values = (2, 4, 6, 8, 10, 12, 14, 16,\
				18, 20, 22, 24, 26, 28, 30, 32,\
				34, 36, 38, 40, 42, 44, 46, 48, 50)

#Loop
while not Terminate:
	
	#User Input and save into int list
	user_list = [int(x) for x in input('Enter numbers:').split()]
	
	#Save only numbers between 1-100
	output = []
	for i in range(len(user_list)):
		if user_list[i] in valid_values:
			output.append(user_list[i])

	#Print the input and output
	print('User input: ', user_list)
	print('Calculated output: ', output)
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True