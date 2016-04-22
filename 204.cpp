/*Generalised Hamming Numbers
Problem 204
A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?*/

#include <stdio.h>
#include <stdlib.h>

#define Factor 5
const unsigned long Max=1000000;
//#define Max 100000000
//#define Max 1000000000

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
	printf("Max = %lu, Factor = %d \n", Max, Factor);
	char Primes[Max]={0};
	printf("Primes array created\n");
	
	for (int i = 2; i < Max; ++i)
		if (isPrime(i)) Primes[i]=1;
	printf("Primes Counting finished.\n");

	int k,fl, Hamming=0;	
	printf("Hamming number = %d\n",Hamming);

	for (int i = 1; i < Max; ++i)
	{
		k = Factor + 1;
		fl = 0;
		if (Primes[i]==0) // if this number is NOT prime 
		{
			while ((fl==0) && (k<i/2)) {
				if ((Primes[k] == 1) && (i % k == 0)) fl=1;
				k++;
			}
			if (fl == 0) Hamming++;//printf("%d\n", i);}
		}
	}
	printf("\nFound %d Hamming numbers\n", Hamming);


	return 0;
}
