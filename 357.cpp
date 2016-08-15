/*Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define N 100000000
// Use miller_rabin test?
int isPrime(int someVal)
{
	if ((someVal%2 == 0) || (someVal%3 == 0)) return 0;
	int newDiv = 5;
	while (someVal % newDiv != 0)
		newDiv += 2;
	//if (newDiv == someVal) printf("Pirme=%ld, ", someVal);
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

int isDprimes(int n){
	if (!(isPrime(n+1))) return 0;
	int dd;
	for (int d = 2; d < n; ++d)
		if (n%d == 0) {
			dd = d + n/d;
			if (!(isPrime(dd))) return 0;
		}
	return 1;
}

int main(int argc, char const *argv[])
{
	const clock_t begin_time = clock();
	unsigned long Sum = 0;
	for (int i = 2; i < N; i += 2)
	{
		if (isDprimes(i)) {
			printf("Found %d\n",i);
			Sum += i;
		}
	}
	printf("Sum (+2 ?) = %li\n", Sum);
	printf("Elasped: %f \n", float( clock () - begin_time ) /  CLOCKS_PER_SEC); 
	return 0;
}
