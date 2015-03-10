/*Truncatable primes
Problem 37
The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only 11 primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.*/

#include <stdio.h>
#include <stdlib.h>

#define Max 1000000

int isPrime(int someVal)
{
	if (someVal < 2) return 0;
	if (someVal<11) if ((someVal == 2) || (someVal == 3) || (someVal == 5) || (someVal == 7)) return 1; else return 0;
	int newDiv=2;
	while (someVal % newDiv != 0)
		newDiv++;
	//if (newDiv == someVal) printf("Prime=%d, ", someVal);
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

int main(int argc, char const *argv[])
{
	int pr=1,dividor,left,right,count=1,Sum=0;
	for (int i = 10; i < Max; ++i)
	{	
		if (isPrime(i)){
			//printf("==%d\n", i);
			dividor=10;
			left=i/dividor;
			right=i%dividor;
			pr=1;
			//from 
			while ((pr) && (left>0)) {
				pr = (isPrime(left) && isPrime(right));
				dividor*=10;
				left=i/dividor;
				right=i%dividor;
				//printf("Next is = %d prime = %d\n",tmp,pr);
			}
		if ((pr) && (left == 0) && (count<=11)) { printf("%d: %d\n",count++, i); Sum+=i;}
		}
	}
	printf("The very Sum = %d\n",Sum);
	return 0;
}

