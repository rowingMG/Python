def getCumulativeGPA():
	max_GPA = 4.3
	
	credits = int(input('Enter total number of earned credits: '))
	while credits <= 0:
		credits = int(input('Enter total number of earned credits(bigger than 0): '))
	cumGPA = float(input('Enter your current cumulative GPA: '))
	while cumGPA > max_GPA or cumGPA < 0:
		cumGPA = float(input('Enter your current cumulative GPA(between 0 ~ 4.3): '))
	sem_credits = int(input('Enter total number of credits of the semaster: '))
	while sem_credits <= 0:
		sem_credits = int(input('Enter total number of credits of the semaster(bigger than 0): '))
	target_GPA = float(input('Enter your target cumulative GPA: '))
	while target_GPA > max_GPA or target_GPA < 0:
		target_GPA = float(input('Enter your target cumulative GPA(between 0 ~ 4.3): '))
	
	cum_info = (credits, cumGPA)
	
	return (cum_info, sem_credits, target_GPA)

		
def findSemasterGPA(cum_info, sem_credits, target_GPA):
	max_GPA = 4.3
	
	cur_credits, cur_cum_GPA = cum_info
	
	cur_quality_pts = cur_credits * cur_cum_GPA
	total_credits = cur_credits + sem_credits
	
	semaster_GPA = (target_GPA * total_credits - cur_quality_pts) / sem_credits
	
	if semaster_GPA < 0:
		semaster_GPA = 0
		cumGPA = cur_quality_pts / total_credits
	elif semaster_GPA > max_GPA:
		semaster_GPA = max_GPA
		cumGPA = (cur_quality_pts + max_GPA * sem_credits) / total_credits
	else:
		cumGPA = target_GPA
	
	return (semaster_GPA, cumGPA)
	
	
##-----MAIN-----##

#Greetings
print('This program calculates semaster and cumulative GPAs\n')

#get cumulative information
cum_info, sem_credits, target_GPA = getCumulativeGPA()
print()

#calculation
semGPA, cumGPA = findSemasterGPA(cum_info, sem_credits, target_GPA) 

#Show results
max_GPA = 4.3

if semGPA <= max_GPA or semGPA >= 0:
	print('Your semaster GPA should', format(semGPA, '.2f'), 'and that gives you', format(cumGPA, '.2f'))
	