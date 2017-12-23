#Age in seconds

import datetime

#Grettings
print('This program calculates your approximate age in seconds.')
print('You can only calculate only after 1900.\n')

#Get User Birthday
birth_year = int(input('Enter your birth year: '))
birth_month = int(input('Enter your birth month: '))
birth_day = int(input('Enter your birth day: '))

#Get Current Days
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

#Calculate
year_difference = current_year - birth_year
month_difference = current_month - birth_month
day_difference = current_day - birth_day
difference_in_sec = (((year_difference * 365) + day_difference) + month_difference * 30) * 24 * 60 * 60

#Result
print('\nYour age in second is approximately', difference_in_sec, 'seconds.')