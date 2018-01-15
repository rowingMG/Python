##4-D1: Morse Code Encryptipn/Decryption Program

##Initialization

Coding = (('a', '·-'), ('b', '-···'), ('c', '-·-·'), ('d', '-··'), ('e', '·'),\
		('f', '··-·'), ('g', '--·'), ('h', '····'), ('i', '··'), ('j', '·---'),\
		('k', '-·-'), ('l', '·-··'), ('m', '--'), ('n', '-·'), ('o', '---'),\
		('p', '·--·'), ('q', '--·-'), ('r', '·-·'), ('s', '···'), ('t', '-'),\
		('u', '··-'), ('v', '···-'), ('w', '·--'), ('x', '-··-'), ('y', '-·--'), ('z', '--··'), ('.', '\n'), (' ', ' '))

Terminate = False


##Loop

while not Terminate:

	#User input, Initialization
	sel = int(input('0 for Encryption, 1 for decryption: '))
	if not sel:
		message = input('Enter the original message: ')
		message = message.lower()
	else:
		message = input('Enter the password: ').split(' ')
	password = ''
	not_sel = abs(sel - 1)
	
	#Encryption/Decryption
	if not sel:
		for ch in message:
			found = False
		
			for t in Coding:
				if ch == t[sel]:
					password = password + t[not_sel] + ' '
					found = True
		
			if not found:
				password = password + ch
	else:
		for i in range(len(message)):
			found = False
			
			for t in Coding:
				if message[i] == t[sel]:
					password = password + t[not_sel]
					found = True
			if message[i] == '' and message[i + 1] == '':
				password = password + format(' ', '1')
					
					
			
	#Print
	print()
	print('The original code is:\n', message, '\n')
	if sel:
		print('The decrypted code is:\n', password, '\n')
	else:
		print('The encrypted code is:\n', password, '\n')
		
	