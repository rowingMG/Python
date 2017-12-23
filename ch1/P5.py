import math

num_city = int(input('How many cities? '))
routes = math.factorial(num_city)
print('For',num_city, 'cities, there are', routes, 'possible routes')