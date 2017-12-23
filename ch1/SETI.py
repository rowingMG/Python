#SETI program
#
#The Drake Equation
#
#	N = R * p * n * f * i * c * L
#

#Display Prompt
print('Welcome to the SETI Program')
print('percentage should be entered as integer')

#get user input
p = int(input('What percentage of stars do you think have planets?'))
n = int(input('How many planets per star do you think can support life?'))
f = int(input('What percentage do you think actually develop life?'))
i = int(input('What percentage of those do you think have intelliget life?'))
c = int(input('What percentage of those do you think can communicate with us?'))
L = int(input('Number of years you think civilizations last?'))

#calculate result
num_detect_civ = 7 * (p/100) * n * (f/100) * (i/100) * (c/100) * L

#display result
print()
print('Based on values entered...')
print('there are estimated', round(num_detect_civ), 'potentially detectable civs.')
