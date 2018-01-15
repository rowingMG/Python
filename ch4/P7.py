##4-P7: Comparing two integer lists

#Initialization
Terminate = False

#Loop
while not Terminate:
	
	#User Input and save into list
	First = input('Enter first int list: ').split()
	Second = input('Enter second int list: ').split()
	First = [int(x) for x in First]
	Second = [int(x) for x in Second]

	#Calculate the result
	if len(First) == len(Second):
		length = ''
	else:
		length = 'not'
		
	if sum(First) == sum(Second):
		summation = ''
	else:
		summation = 'not'
		
	for i in range(len(First)):
		if First[i] in Second:
			occur_both = 'some'
			break
		else:
			occur_both = 'not any'
	
	#Print the input and output
	print()
	print('User input: ', First, Second)
	
	print('The length of the two lists are', length, 'same.')
	print('The sum of each two lists are', summation, 'same.')
	print('There is', occur_both, 'values that occur in both lists.')
	
	#Ask for redo
	terminate_val = input('Do you want to terminate?(put y for yes): ')
	if terminate_val == 'y':
		Terminate = True