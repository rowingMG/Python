def grettings():
	print('이 프로그램은 신용카드 대금과 이자를 갚는 데 걸리는 시간을')
	print('총 금액과 이율에 기반하여 계산해 주는 프로그램입니다.')

	
def getLoanInfo():
	print()
	balance = float(input('총 신용카드 대금을 입력하세요: '))
	int_rate = float(input('신용카드 연 이율을 입력하세요: '))
	
	return (balance, int_rate)
	
	
def calculateMinPay(balance):
	print()
	
	abs_minimum = 20000
	pay_rate = 2
	
	rel_minimum = int((pay_rate / 100) * balance)
	
	print('총 상환금액의', str(pay_rate) + '%', '를 최소상환금액으로 합니다.(잔고에 상관없이 최소 20000원)')
	if abs_minimum < rel_minimum:
		print('최소상환금액은', rel_minimum, '원 입니다.') 
		return rel_minimum
	else:
		print('최소상환금액은', abs_minimum, '원 입니다.') 
		return abs_minimum


def determineMonthlyPay(minimum_pay):
	print()
	
	valid_response = True
	
	response = input('최소 금액 지불을 사용하시겠습니까? (y/n): ')
	while valid_response:
		if response in ('y', 'Y'):
			return minimum_pay
		elif response in ('n', 'N'):
			monthly_pay = float(input('매 달 상환할 금액을 입력하세요: '))
			return monthly_pay
		else:
			response = input('올바른 입력을 선택하세요(y/n): ')
			print()
			

def calculatePayoff(monthly_pay, balance, interest_rate):
	empty_tab = format(' ', '6')
	int_rate_month = (interest_rate / 100) / 12
	print(int_rate_month)
	
	print()
	print(empty_tab, '상환 계획')
	print(empty_tab, format('년차', '6s'), format('잔액', '10s'), format('상환 회차', '14s'), format('총 상환 이자', '14s'))
	
	year = 1
	cur_balance = balance
	payment_num = 1
	interest_paid = 0
	
	while cur_balance > 0:
		interest = int_rate_month * cur_balance
		cur_balance = cur_balance + interest - monthly_pay
		interest_paid = interest_paid + interest
		if cur_balance < 0:
			cur_balance = 0
		
		if payment_num % 12 == 1:
			print(empty_tab, format(year, '6d'), format(cur_balance, '10.0f'), format(payment_num, '14d'), format(interest_paid, '14.0f'))
			year = year + 1
		else:
			print(empty_tab, empty_tab, format(cur_balance, '10.0f'), format(payment_num, '14d'), format(interest_paid, '14.0f'))

		payment_num = payment_num + 1
		

##----MAIN----##
grettings()

do_calculation = True

while do_calculation:
	
	balance, interest_rate = getLoanInfo()
	
	min_pay = calculateMinPay(balance)
	
	monthly_pay = determineMonthlyPay(min_pay)
	
	calculatePayoff(monthly_pay, balance, interest_rate)
	
	response = input('다른 상환에 대해 다시 계산하시겠습니까? (y/n): ')
	while response not in ('n', 'N', 'y', 'Y'):
		response = input('올바른 입력을 선택하세요(y/n): ')
	if response in ('n', 'N'):
		do_calculation = False
			
	