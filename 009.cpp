/*A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define max 1000

int main(int argc, char const *argv[])
{
	double val;
	for (int a = 1; a < max; ++a)
		for (int b = a; b < max; ++b)
			for (int c = b; c < max; ++c) {
				if (a+b+c == max) {
					//printf("%d + %d + %d = %d\n", a,b,c,a+b+c);
					if (a*a + b*b == c*c)
					{printf("%d^2 + %d^ = %d^2\tAnswer = %d\n",a,b,c,a*b*c);}
				}
			}

	return 0;
}
