//gcc 066.cpp -lm 
#include "stdio.h"
#include "stdlib.h"
#include <math.h>

int isSquare(int D){
	if ( int(pow( (int(sqrt(D))),2)) == D) 
		return 1;
	else 
		return 0;
}

int tryBroot(){
	long x,y;
	long x2,y2,equat;
	for (int D = 600; D <= 670; ++D)
	{
		if (isSquare(D)) continue;
		x = (int)sqrt(D);
		while (1) {
			y = 1;
			x2 = x*x;
			y2 = D*y*y;
			equat = x2 - y2;
			//printf("%ld^2 - %d* %ld^2 ? 1\n",x,D,y);
			while ( equat > 1 ) {
				y++;
				x2 = x*x;
				y2 = D*y*y;
				equat = x2 - y2;
			//	printf("%ld^2 - %d* %ld^2 = %ld -%d* %ld  = %ld ? 1\n",x,D,y,x2,D,y2,equat);
			}
			if ( equat == 1 ){
				printf("===== %ld^2 - %d* %ld^2 = 1\n",x,D,y);
				break;
			}
			//printf("D = %d, x = %d, y = %d\n",D,x,y);
			x++;
		}
	}
}

int main(int argc, char const *argv[])
{
	unsigned long x,y,xMax=0;
	unsigned long long x2,y2;
	int Dmax=0;
	for (int D = 3; D <= 1000; ++D)
	{
		if (isSquare(D)) continue;
		//printf("D = %d\n", D);
		x = (int)sqrt(D)+1;
		while (1){
			x2 = x*x - 1;
			if (x2 % D == 0) {
				y2 = x2 / D;
				if ( isSquare(y2) ) {
					printf("%d %ld\n",D,x);
					//printf("%11ld^2 - %4d* %11d^2 = 1\n",x,D,(int)sqrt(y2));
					//printf("print %ld**2 - %d*%d**2\n",x,D,(int)sqrt(y2));
					if (x > xMax) {xMax = x; Dmax = D;}
					break;
				}
			}
			x++;
		}
	}
	printf("Dmax = %d with x = %ld\n",Dmax,xMax);
	
	return 0;
}
