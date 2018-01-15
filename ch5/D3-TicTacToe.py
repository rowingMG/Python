##############################
##Tic-Tac-Toe 게임(3x3 빙고)##
##############################

####단판 게임에 관한 함수들####

def initializeGame(previous_start_player):
	game_info = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	turn = 1
	player = ( previous_start_player % 2 ) + 1
	winner = 0
	
	return (game_info, turn, player, winner)

def updateGame(game_info, player, coordinates):
	x, y = coordinates
	
	if player == 1:
		game_info[y][x] = 1
	else: #if player is 2
		game_info[y][x] = -1
	
	return game_info

def updateTurn(turn):
	return turn + 1

def updatePlayer(player):
	#1은 2로 2는 1으로
	return ( player % 2 ) + 1

def getSingleCoordinate(x_or_y):
	coordinate = int(input(x_or_y + '좌표를 입력하세요: '))
	while coordinate not in (0, 1, 2):
		coordinate = int(input(x_or_y + '좌표를 입력하세요(0 ~ 2): '))
	
	return coordinate
	
def getCoordinates(game_info, player):
	x = getSingleCoordinate('x')
	y = getSingleCoordinate('y')
	
	while game_info[y][x] != 0:
		print('이미 말이 있습니다. 다른 좌표를 선택하세요.\n')
		x = getSingleCoordinate('x')
		y = getSingleCoordinate('y')
		
	return (x, y)

def returnWinner(line_sum):
	if line_sum == 3:
		return 1
	elif line_sum == -3:
		return 2

def whoIsWinner(game_info):
	for i in range(3):
		#가로
		x_sum = sum(game_info[i])
		if abs(x_sum) == 3:
			return returnWinner(x_sum)
		
		#세로
		y_sum = 0
		for j in range(3):
			y_sum = y_sum + game_info[j][i]
		if abs(y_sum) == 3:
			return returnWinner(y_sum)
	
	#대각선
	dig_sum_1 = game_info[0][0] + game_info[1][1] + game_info[2][2]
	if abs(dig_sum_1) == 3:
		return returnWinner(dig_sum_1)
	
	dig_sum_2 = game_info[2][0] + game_info[1][1] + game_info[0][2]
	if abs(dig_sum_2) == 3:
		return returnWinner(dig_sum_2)
	
	#이도저도 아니면 무승부
	return 0

	
##Display 관련 함수들##

def displayGame(game_info):
	empty_num = format(' ', '10')
	neutral = '- '
	player_1 = 'O '
	player_2 = 'X '
	
	display = [[neutral for x in range(3)] for y in range(3)]
	
	#display를 game info에 맞게 업데이트하는 코드
	for i in range(3):
		for j in range(3):
			if game_info[i][j] == 1:
				display[i][j] = player_1
			elif game_info[i][j] == -1:
				display[i][j] = player_2
	
	#display를 화면에 print하는 코드
	print()
	for i in range(3):
		print(empty_num, end = '')
		for j in range(3):
			print(display[i][j], end = '')
		print()
	print()

def displayTurnInfo(player):
	print('플레이어', player, '의 차례입니다.')

def displayWinnerInfo(winner):
	if winner != 0:
		print('플레이어', winner, '의 승리입니다!')
	else:
		print('무승부입니다!')


####기록과 게임 지속 여부에 대한 함수들####

def initializeRecord():
	return [0, 0, 0]

import random

def initializePlayer():
	return rand.randint(1, 3)

def updateRecord(winner, record):
	if winner == 1:
		record[0] = record[0] + 1
	elif winner == 2:
		record[2] = record[2] + 1
	else:
		record[1] = record[1] + 1
	
	return record

def displayRecord(record):
	print('현재까지의 전적은', str(record[0]) + '승',
		str(record[1]) + '무', str(record[2]) + '패', '입니다.\n')

def AskforContinue():
	response_yes = ('y', 'Y')
	response_no = ('n', 'N')
	
	response = input('게임을 계속하시겠습니까?(y/n): ')
	while response not in response_no + response_yes:
		response = input('y/n 중 고르세요: ')

	if response in response_yes:
		return True
	else:
		return False
		
		
##################		
##-----Main-----##
##################

print('-----Tic Tac Toe Game-----')

game_continue = True
record = initializeRecord()
player = initializePlayer()

while game_continue:
	game_info, turn, player, winner = initializeGame(player)
	displayGame(game_info)

	while winner == 0 and turn < 9:
		displayTurnInfo(player)
		
		coordinates = getCoordinates(game_info, player)
		
		game_info = updateGame(game_info, player, coordinates)
		turn = updateTurn(turn)
		player = updatePlayer(player)
		
		displayGame(game_info)
		
		winner = whoIsWinner(game_info)
		
	displayWinnerInfo(winner)
	
	record = updateRecord(winner, record)
	displayRecord(record)
	
	game_continue = AskforContinue()