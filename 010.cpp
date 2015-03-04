/*The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

#include <stdio.h>
#include <stdlib.h>

#define Limit 2000000

int main(int argc, char const *argv[])
{
	int Grid[Limit];
	unsigned long Sum=0;
	for (int i = 0; i < Limit; ++i)
		Grid[i]=i;
	int step=Limit/1000,next=step,per=1;
	for (int i = 2; i < Limit; ++i)
	{
		for (int j = i+1; j < Limit; ++j)
			if (j%i == 0) Grid[j]=0;
		if (i>next) {printf("%d \n",per++);next+=step;}
	}

	//for (int i = 0; i < Limit; ++i)	printf("%d, ", Grid[i]);


	for (int i = 2; i < Limit; ++i)
	{
		Sum+=Grid[i];
	}
	printf("\nSum = %ld\n", Sum);

}

