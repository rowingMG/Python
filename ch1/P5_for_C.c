#include <stdio.h>

int factorial(int x)
{
	int i, result = 1;
	
	for(i = 1; i <= x; i++)
		result *= i;
	
	return result;
	
int main(void)
{
	int city, routes;
	
	printf("How many cities?\n");
	scanf("%d", &city);

	routes = factorial(city);
	printf(For %d cities, there are %d possible routes\n", city, routes);
	
	return 0;
}