/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/
#include <stdio.h>
#include <stdlib.h>

#define MAX 28123

int Abundant[7000];

int searchAbundant(){
	int Sum=1;
	int cnt=0;
	for (int i = 1; i < MAX; ++i)
	{
		Sum = 1;
		for (int d = 2; d <= i/2; ++d)
			if ( i%d == 0) Sum += d;
		if (Sum > i) {/*printf("%d abundant\n",i);*/ Abundant[cnt] = i; cnt++;}
	}
	printf("cnt = %d\n",cnt );
	return cnt;
}

// checks if the number can be written as sum of Abundant numbers
bool check(int val){
	//printf("Processing %d\n", val);
	int cntA=0,cntA2;
	while (val > Abundant[cntA]){
		cntA2 = cntA;
		while (Abundant[cntA] + Abundant[cntA2] <= val){
			if ( Abundant[cntA] + Abundant[cntA2] == val) return true;
			cntA2++;
		}
		cntA++;
	}
	return false;
}

int main(int argc, char const *argv[])
{
	int cntA = searchAbundant();
	long int Sum=0;
	for (int i = 1; i < 28124; ++i)
	{
			if (!check(i)) Sum += i;
	}
	printf("Sum = %ld\n", Sum);
	return 0;
}