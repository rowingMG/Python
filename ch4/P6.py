##4-P6: Listing fruits and its weight

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into list
	Endlist = False
	Fruits = []
	while not Endlist:
		fruit = input('Enter fruit(put x for terminate): ')
		if fruit != 'x':
			weight = int(input('Enter weight of %s: ' % fruit))
			Fruits = Fruits + [[fruit, weight]]
		else:
			Endlist = True
		

	#Print the input and output
	print()
	print('User input: ', Fruits)
	
	for i in range(len(Fruits)):
		print('%s, %d lbs.' % (Fruits[i][0], Fruits[i][1]))
	print('etc.')
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True