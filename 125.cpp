/*Palindromic sums
Problem 125
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly 11 palindromes below 1000 that can be written as consecutive square sums, and the sum of these palindromes is 4164. 
Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.*/

#include <stdio.h>
#include <stdlib.h>
#include "usefullFunctions.h"

#define Maxed 100000000

int main(int argc, char const *argv[])
{
	int cnt=0, k;
	unsigned long gSum=0,Sum;
	unsigned long Arr[200]={0};
	for (int i = 1; i*i < Maxed; ++i)
		{	k=i+1;
			Sum=i*i;
			while (Sum < Maxed)
			{
				Sum+=k*k;
				if ((Sum<Maxed) && (isPalindrom(Sum))) { 
					printf("%d(for i=%d, k=%d): %lu\n", cnt,i,k,Sum); 
					Arr[cnt]=Sum; 
					gSum+=Sum;cnt++;
				}
				k++;
			}	
		}	
	printf("gSum = %lu\n", gSum);
	// The problem is there are some repeated values, so we have to eleminate them
	for (int i = 0; i < cnt-1; ++i)
	{
		for (int j = i+1; j < cnt; ++j)
		{
			if (Arr[i]==Arr[j]) { printf("%d and %d = %lu Ahtung!!\n",i,j, Arr[i]); gSum-=Arr[j];}
		}
	}
	printf("gSum = %lu\n", gSum);
	return 0;
}

