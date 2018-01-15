##4-P4: Count numbers of 'a' appears on the names

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into list
	user_names = [str(x) for x in input('Enter first names: ').split()]
	
	#Increment cnt if 'a' appears
	cnt = 0
	for i in range(len(user_names)):
		if 'a' in user_names[i]:
			cnt = cnt + user_names[i].count('a')

	#Print the input and output
	print()
	print('User input: ', user_names)
	if cnt == 0:
		print("There aren't any 'a' in the list.")
	elif cnt == 1:
		print("There is 1 'a' in the list.")
	else:
		print('There are', cnt, "'a's in the list.")
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True