#include "stdio.h"
#include "stdlib.h"

int divSum(int n)
{
	int Sum = 0;
	for (int i = 1; i < n; ++i)
		if (n%i == 0) Sum+=i;
	return Sum;
}

int main(int argc, char const *argv[])
{
	int Sum = 0;
	for (int i = 2; i < 10000; ++i)
	{
		
		if (i == divSum(divSum(i)))
			if (i != divSum(i)) {
				printf("%d is amicable to %d\n",i,divSum(i) ); 
				Sum += i;
			}
	}
	printf("Sum = %d\n",Sum);
}