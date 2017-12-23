#Converting farenheight and celcius

#Grettings and info
print('Enter F to convert farenheight to celcius')
print('Enter C to convert celcius to farenheight')

#User input
which = input('Enter F or C: ')
while (which != 'F' and which != 'C'):
	which = input('Invalid. Enter F or C: ')
	
temp = int(input('Enter temperature you selected: '))

#Calculate and print
if which == 'F':
	converted_temp = (temp - 32) * 5/9
	print(temp, 'F is', converted_temp, 'C.')
else:
	converted_temp = (9/5 * temp) + 32
	print(temp, 'C is', converted_temp, 'F.')