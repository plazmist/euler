/*The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/


#include <stdio.h>
#include <stdlib.h>

#define steps 1000000

int main(int argc, char const *argv[])
{
	unsigned long res,iMax;
	unsigned int cnt=0,Max=0;

	for (int i = 2; i < steps; ++i)
	{
		cnt=0;
		res=i;
		while (res != 1) {
			if (res%2 == 0) res/=2;
			else res=res*3+1;
			cnt++;
			//printf("%d -> ", res);
		}
		if (cnt > Max) {Max=cnt; iMax=i;}
		//printf("\nChain for %d ended with %d steps\n", i, cnt);
	}
	printf("iMax = %d in %d steps\n", iMax,Max);
	return 0;
}