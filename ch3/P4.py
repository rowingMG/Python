#ch3 P4

num = 1
terminate = ''

while terminate != 'n':
	total = 0
	while num != -1:
		num = int(input('Enter any positive integer(-1 to terminate): '))
		if num < 100 and num != -1:
			total = total + num
	
	print('The total is', total)
	
	terminate = input('Press n to terminate...')
	