#ch3 P7 Displays 1 to 100 in 10X10 matrix format

num = 1

while num <= 100:
	print('{:3}'.format(num), end = '')
	if not num % 10:
		print()
	num = num + 1