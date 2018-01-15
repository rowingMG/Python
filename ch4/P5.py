##4-P5: Saves only those words whose first letter occurs again within the word

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into list
	user_words = [str(x) for x in input('Enter words: ').split()]
	low_user_words = [user_words[i].lower() for i in range(len(user_words))]
	#Increment cnt if 'a' appears
	output = []
	for i in range(len(low_user_words)):
		first_letter = low_user_words[i][0]
		if first_letter in low_user_words[i][1:]:
			output.append(user_words[i])

	#Print the input and output
	print()
	print('User input: ', user_words)
	print('Output:     ', output)
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True