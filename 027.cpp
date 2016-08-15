#include <stdio.h>
#include <stdlib.h>
#include "usefullFunctions.h"

int main(int argc, char const *argv[])
{
	int n,D,maxN=0;
	for (int a = -999; a < 1000; ++a)
		for (int b = -1000; b < 1001; ++b)
		{
			n = 0;
			D = n*n +a*n + b;
			//printf("START a=%d b=%d n=%d, D = %d\n",a,b,n,D );
			while ((D > 0) && (isPrime(D))){
				//printf("YES a=%d b=%d n=%d, D = %d\n",a,b,n,D );
				D = n*n +a*n + b;
				n++;
			}
			if (n > maxN) { maxN = n; printf("maxN = %d, a = %d,b = %d, (%d)\n",n,a,b,a*b );}
		}
	return 0;
}
