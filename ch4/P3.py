##4-P3: By getting user input, save as numbers for under 100, save 'over' for over 100

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into int list
	user_list = [int(x) for x in input('Enter numbers: ').split()]
	
	#Save only numbers between 1-100
	output = []
	for i in range(len(user_list)):
		if user_list[i] > 100:
			output.append('over')
		else:
			output.append(user_list[i])

	#Print the input and output
	print()
	print('User input:        ', user_list)
	print('Calculated output: ', output)
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True