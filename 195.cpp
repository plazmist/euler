#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int trgl(int R_limit,int bak)
{
	int a = 1,b = a+1;
	int kMAX=0,k;
	double c,r = 0;
	int T = 0;
	while (r <= R_limit)
	{
		r = 0;
		while ((r <= R_limit) && (b < (bak*a))) 
		{
			c = sqrt(a*a + b*b - a*b);
			if (c == floorf(c)){
				r = a*b*sqrt(3)/(2.*(a+b+c));
				if (r <= R_limit) {
					k = b/a;
					if (k > kMAX) kMAX = k;
					T++; 
					printf("Found ( %d %d %.1f ) \n",a,b,c );
				}
			}
			b++;
		}
		a++;
		b = a+1;
		c = sqrt(a*a + b*b - a*b);
		r = a*b*sqrt(3)/(2.*(a+b+c));
		//printf("r end = %.2f\n", r);
	}
	printf("b/a = %d, T( %d ) = %d kMAX = %d\n", bak,R_limit, T,kMAX);

}

int main(int argc, char const *argv[])
{
	trgl(1000,2000);
	
}