#P1
def zeroCheck(first, second, third):
	if first * second * third == 0:
		return True
	else:
		return False
		
#P2
def ordered3(first, second, third):
	if (first, second, third) == tuple(sorted([first, second, third])):
		return True
	else:
		return False

#P3
def modCount(first, second):
	if first <= second:
		m = first
		n = second
	else:
		n = first
		m = second
	
	count = 0
	for i in range(1, n):
		if i % m == 0:
			count = count + 1
	
	return count

#P4
def helloWorld(name):
	print('Hello World, my name is', name)
	
#P5
def printAsterisks(n):
	if n > 75:
		print('*' * 75)
	else:
		print('*' * n)

#P6
def getContinue():
	response_yes = ('y', 'Y')
	response_no = ('n', 'N')
	
	response = input('Do you want to continue (y/n): ')
	while response not in response_yes + response_no:
		response = input('Do you want to continue (choose among y/n): ')
	
	if response in response_yes:
		return 'y'
	else:
		return 'n'

#P7
def truncate(list, threshold):
	for i in range(len(list)):
		if list[i] > threshold:
			list[i] = 0
	
	return list
	
#P8
def truncate_v2(list, threshold):
	newlist = []
	for k in list:
		if k > threshold:
			newlist.append(0)
		else:
			newlist.append(k)
	
	return newlist

	
##---Main---##
#P1
print()
print(zeroCheck(1, 2, 10))
print(zeroCheck(1, 0, 10))

#P2
print()
print(ordered3(1, 2, 10))
print(ordered3(2, 1, 10))

#P3
print()
print(modCount(10, 3))

#P4
print()
helloWorld('myeonggil')

#P5
print()
printAsterisks(10)
printAsterisks(30)
printAsterisks(100)

#P6
print()
print(getContinue())

#P7, P8
print()
list = [1, 3, 4, 6, 7, 9, 12, 34, 3, 12, 7]
print(truncate(list, 10))
print(truncate_v2(list, 10))
