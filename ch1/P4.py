#Change 4 digit binary number to decimal number

fourth = int(input('Enter leftmost digit: '))
third = int(input('Enter the next digit: '))
second = int(input('Enter the next digit: '))
first = int(input('Enter the next digit: '))
result = fourth * (2**3) + third * (2**2) + second * (2**1) + first * (2**0)
print('The value is', result)
