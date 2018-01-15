##4-P1: Save only number between 1-100 for user input list

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into int list
	user_list = [int(x) for x in input('Enter numbers:').split()]
	
	#Save only numbers between 1-100
	output = []
	for i in range(len(user_list)):
		if user_list[i] >= 1 and user_list[i] <= 100:
			output.append(user_list[i])

	#Print the input and output
	print('User input: ', user_list)
	print('Calculated output: ', output)
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True