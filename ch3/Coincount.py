#add up the coins until values reaches to a displayed value.

import random

#initialize
terminate = False
empty_str = ''

#main part
while not terminate:
	total = 0
	amount = 10 * random.randint(1,99)
	print('Enter coins add up to', amount, 'KRW, one per line\n')
	game_over = False
	
	while not game_over:
		valid_coin = False
		
		while not valid_coin:
			if total == 0:
				coin = input('Enter the first coin: ')
			else:
				coin = input('Enter next coin: ')
			
			if coin in (empty_str, '10', '50', '100', '500'):
				valid_coin = True
			else:
				print('Invalid coin')
		
		if coin == empty_str:
			if total == amount:
				print('Correct!!')
			else:
				print('You only entered', total, 'wons.')
			
			game_over = True
		else:
			total = total + int(coin)
			if total > amount:
				print('You excedeed', total - amount, 'wons.')
				game_over = True
				
		if game_over:
			coin = input('\nPress any key to continue...(n for terminate)')
			
			if coin == 'n':
				terminate = True

print('Thanks for playing.')
			