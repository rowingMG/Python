def isFirst():

	response_yes = ('y', 'Y')
	response_no = ('n', 'N')
	
	response = input('Is this your First semaster?(y/n): ')
	while response not in response_no + response_yes:
		response = input('Is this your First semaster?(select among y/n): ')
	
	if response in response_yes:
		return True
	else:
		return False
		
		
def getCumulativeGPA():

	credits = int(input('Enter total number of earned credits: '))
	cumGPA = float(input('Enter your current cumulative GPA: '))
	
	return (credits, cumGPA)

	
def getGrades():

	semaster_info = []
	more_grades = True
	empty_str = ''
	
	while more_grades:
		grade = input('Enter grade (hit enter if done): ')
		while grade not in ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', empty_str):
			grade = input('Enter correct grade (hit enter if done): ')
		if grade == empty_str:
			more_grades = False
		else:
			credit = int(input('Enter number of credits: '))
			semaster_info.append([credit, grade])
		
	return semaster_info
		
		
def convertGrade(grade):

	if grade == 'A+':
		return 4.3
	elif grade == 'A':
		return 4
	elif grade == 'A-':
		return 3.7
	elif grade == 'B+':
		return 3.3
	elif grade == 'B':
		return 3
	elif grade == 'B-':
		return 2.7
	elif grade == 'C+':
		return 2.3
	elif grade == 'C':
		return 2
	elif grade == 'C-':
		return 1.7
	elif grade == 'D+':
		return 1.3
	elif grade == 'D':
		return 1
	elif grade == 'D-':
		return 0.7
	else:
		return 0

		
def calculateTotalGPA(cumulated_info, semaster_info):
	
	cur_credits, cur_cum_GPA = cumulated_info
	
	cur_quality_pts = cur_credits * cur_cum_GPA
	
	sem_quality_pts = 0
	sem_credits = 0
	
	for i in range(len(semaster_info)):
		credit, letter_grade = semaster_info[i]
		numeric_grade = convertGrade(letter_grade)
		sem_credits = sem_credits + credit
		sem_quality_pts = sem_quality_pts + credit * numeric_grade
	semGPA = sem_quality_pts / sem_credits
	
	tot_quality_pts = cur_quality_pts + sem_quality_pts
	tot_credits = cur_credits + sem_credits
	totGPA = tot_quality_pts / tot_credits
	
	return (semGPA, totGPA)
	
	
##-----MAIN-----##

#Greetings
print('This program calculates semaster and cumulative GPAs\n')

#IsFirst?
is_first = isFirst()

#get cumulative information
if is_first:
	cum_info = (0, 0)
else:
	cum_info = getCumulativeGPA()
print()

#get the semester info
sem_info = getGrades()
print()

#calculation
semGPA, totGPA = calculateTotalGPA(cum_info, sem_info)

#Show results
print('Your semaster GPA is', format(semGPA, '.2f'))
print('Your new cumulative GPA is', format(totGPA, '.2f'))