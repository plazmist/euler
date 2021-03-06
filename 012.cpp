/*The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
*/


#include <stdio.h>
#include <stdlib.h>

#define count 20

int Dividors(unsigned long Val)
{
	int cnt=0;
	for (unsigned long i = 1; i <= Val; ++i)
		if (Val%i == 0) cnt++;
	return cnt;
} 


int main(int argc, char const *argv[])
{
	unsigned long Sum=0;
	int cnt1=20;
	int cnt2=400000;
	int div;
	// 5983 - 17901136: 80
	// 5984 - 17907120: 480
	Sum = 17877210;
	for (int i = 5980; ; ++i)
		{
			Sum+=i;
			div = Dividors(Sum);
			printf("%d - %ld: %d\n", i, Sum, div);
			if ( div >= 500 ) return 0;
			//if (Dividors(Sum)>500){
				//printf("+%d = %ld: \n",i,Sum);
				//printf("%ld: %d\n",Sum, Dividors(Sum));
			//	return 0;
		//	}
		}	
/*	for (int i = cnt1; i < cnt2; ++i)
	{
		Sum+=i;
		printf("+%d = %ld: %d\n",i,Sum, Dividors(Sum));
	}*/
	return 0;
}
