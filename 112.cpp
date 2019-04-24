#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

int bouncy(int n){
	int decr=1,incr =1,l0,l1;
	l0 = n%10;
	n = n/10;
	//incr
	while ((n > 0) && (decr || incr)){
		l1 = n%10;
		if (decr && (l0 >= l1)) decr = 1;
			else decr = 0;
		if (incr && (l0 <= l1)) incr = 1;
			else incr = 0;
		l0 = l1;
		n = n/10;
	}
	if (!decr && !incr) return 1;
	return 0;
}

int main(int argc, char const *argv[])
{
	int bnc = 0;
	int N = INT_MAX/1024;
	for (int i = 1; i < N; ++i)
	{
		if (bouncy(i)) bnc++;
		if (100.*bnc/i >= 99.0) {printf("N = %d Bouncy = %4.2f\n", i,100.*bnc/i); break;}
	}
	return 0;
}