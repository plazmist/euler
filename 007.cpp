//By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//What is the 10 001st prime number?


#include <stdio.h>
#include <stdlib.h>
#define nPrime 10001

int isPrime(unsigned long someVal)
{
	unsigned long newDiv=2;
	while (someVal % newDiv != 0)
		newDiv++;
	//if (newDiv == someVal) printf("Prime=%ld, ", someVal);
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

int main(int argc, char const *argv[])
{
	unsigned long val=2;
	for (int i = 1; i <= nPrime; ++i)
	{
		while (!isPrime(val)) val++;
		printf("%d=%ld, ",i,val);
		val++;
	}
	printf("\nThe %d = %ld\n",nPrime,val-1);
	return 0;
}
